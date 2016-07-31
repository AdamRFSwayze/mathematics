function clean_corpus(text, regex; normalize = true, lower_case = true)
    if normalize
        # replace control characters with spaces
        text = normalize_string(text, stripmark = true, stripignore = true, stripcc = true)
    end

    if lower_case
        text = lowercase(text)
    end

    # remove unwanted characters
    text = replace(text, regex, "")

    # remove ""
    text = split(text)
    target_index = 1
    for i in 1:length(text)
        target_index = findnext(text, "", target_index)
        if target_index == 0
            break
        else
            splice!(text, target_index)
        end
    end
    text = join(text, " ")
end

function text_to_numeric(text, symbols)
    numeric_text = []
    for each in text
        push!(numeric_text, findfirst(symbols, each))
    end

    numeric_text
end

function numeric_to_text(numeric, symbols)
    text= []
    for num in numeric
        push!(text, symbols[num])
    end

    text
end

function get_corpus_frequencies(corpus, ngram; groupby = "words")
    # to get frequency of symbol x after ngram symbols
    ngram = ngram + 1
    if groupby == "chars"
        corpus = split(corpus, "")
    else
        corpus = split(corpus)
    end

    # find unique symbols
    unique_symbols = unique(corpus)
    # convert text to numbers
    corpus_numeric = text_to_numeric(corpus, unique_symbols);
    # create M
    dimensions = repeat([length(unique_symbols)], outer=[ngram])
    M = repeat(zeros(UInt16, 1), outer = dimensions)
    # get frequencies for ngram of text
    for i in 1:length(corpus)-ngram+1
        M[corpus_numeric[i:i+ngram-1]...] += 1
    end

    M
end

function choose_next_state(distribution, r)
    # only consider entries that are non-zero
    nonzero_entries = findn(distribution)

    distribution_nonzero = distribution[nonzero_entries]
    ranges = cumsum(distribution_nonzero)

    for (idx, range) in enumerate(ranges)
        if r < range
            return nonzero_entries[idx]
        end
    end
end

function trickle_down(current_state, M)
    none_worked = true
    for (idx, P) in enumerate(M)
        sigma = convert(Int, sum(P[current_state[idx:end]..., :][:]))
        if sigma != 0 # avoid division by 0 error
            distribution = P[current_state[idx:end]..., :][:] /
                           sum(P[current_state[idx:end]..., :][:])
            r = rand()
            next_word_idx = choose_next_state(distribution, r)
            none_worked = false
            break
        end
    end
    if none_worked
        # just choose next state at random
        next_word_idx = rand(1:length(M[1][current_state..., :][:]))
    end

    next_word_idx
end

function markov_model(ϕ, num_steps, unique_symbols, ngram, M, groupby)
    if groupby == "chars"
        ϕ = split(ϕ, "")
    else
        ϕ = split(ϕ)
    end

    # create empty array to store result of Markov jumping from state to state
    markov_chain_text = []
    append!(markov_chain_text, ϕ)

    current_state = text_to_numeric(ϕ, unique_symbols)

    # "trickle-down" transition matrices
    for step in 1:num_steps
        next_word_idx = trickle_down(current_state, M)
        next_word = numeric_to_text([next_word_idx], unique_symbols)[1]
        push!(markov_chain_text, next_word)
        current_state = text_to_numeric(markov_chain_text[end-ngram+1:end], unique_symbols)
    end

    markov_chain_text
end

function get_phi(cleaned_corpus, ngram; groupby = "words")
    if groupby == "chars"
        cleaned_corpus_array = split(cleaned_corpus, "")
    else
        cleaned_corpus_array = split(cleaned_corpus)
    end
    starting_point = rand(1:length(cleaned_corpus_array)-ngram)
    ϕ = join(cleaned_corpus_array[starting_point:starting_point+ngram-1], " ")
end

function run(corpus, M; num_steps = 10, ngram = 2, groupby = "words")
    unique_symbols = unique(split(corpus))
    # choose random ngram set of symbols from text
    ϕ = get_phi(corpus, ngram, groupby = groupby)
    @show ϕ

    markov_chain_text = markov_model(ϕ, num_steps, unique_symbols, ngram, M, groupby)
    join(markov_chain_text, " ")
end

function prepare_books()
    f = open("mark_twain_books/adventures_of_tom_sawyer.txt")
    ats = readall(f);
    # create regex object (I prefer whitelisting characters I want to keep)
    chars_to_remove = r"[^a-z ]"
    ats_clean = clean_corpus(ats, chars_to_remove);
    # import other books
    f = open("mark_twain_books/huckleberry_finn.txt")
    hf = readall(f)
    f = open("mark_twain_books/the_prince_and_the_pauper.txt")
    tpatp = readall(f)
    # clean other books
    hf_clean = clean_corpus(hf, chars_to_remove)
    tpatp_clean = clean_corpus(tpatp, chars_to_remove)

    # combine all books
    big_corpus_clean = ats_clean * " " * hf_clean * " " * tpatp_clean

    # for ngram = 2
    len_ats_clean = length(split(ats_clean))
    ats_subset = join(split(ats_clean)[1:round(Int64, len_ats_clean/45)], " ")
    len_hf_clean = length(split(hf_clean))
    hf_subset = join(split(hf_clean)[1:round(Int64, len_hf_clean/45)], " ")
    len_tpatp_clean = length(split(tpatp_clean))
    tpatp_subset = join(split(tpatp_clean)[1:round(Int64, len_tpatp_clean/45)], " ")
    sub_corpus_clean_2 = ats_subset * " " * hf_subset * " " * tpatp_subset;

    # for ngram = 3
    len_ats_clean = length(split(ats_clean))
    ats_subset = join(split(ats_clean)[1:round(Int64, len_ats_clean/540)], " ")
    len_hf_clean = length(split(hf_clean))
    hf_subset = join(split(hf_clean)[1:round(Int64, len_hf_clean/540)], " ")
    len_tpatp_clean = length(split(tpatp_clean))
    tpatp_subset = join(split(tpatp_clean)[1:round(Int64, len_tpatp_clean/540)], " ")
    sub_corpus_clean_3 = ats_subset * " " * hf_subset * " " * tpatp_subset;

    return big_corpus_clean, sub_corpus_clean_2, sub_corpus_clean_3
end

# ------------ EXPERIMENTS ------------ #
big_corpus_clean, sub_corpus_clean_2, sub_corpus_clean_3 = prepare_books()
ts = transition_matrices

println("ngram = 1")
println("# of states = 16,539")
ngram1results = run(big_corpus_clean, ts, num_steps = 200, ngram = 1);
println(ngram1results)

# println("ngram = 2")
# println("# of states = 1,452")
# ngram2results = run(sub_corpus_clean_2, ts, num_steps = 200, ngram = 2);
# println(ngram2results)

# println("ngram = 3")
# println("# of states = 242")
# ngram3results = run(sub_corpus_clean_3, ts, num_steps = 200, ngram = 3);
# println(ngram3results)
