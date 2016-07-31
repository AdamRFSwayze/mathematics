using JLD

M_3 = load("data/ngram=3/M_3.jld", "M_3")
M2forM3 = load("data/ngram=3/M2forM3.jld", "M2forM3")
M1forM3 = load("data/ngram=3/M1forM3.jld", "M1forM3")

transition_matrices = tuple(M_3, M2forM3, M1forM3)
