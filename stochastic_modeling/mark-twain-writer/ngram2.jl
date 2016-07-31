using JLD

M_2 = load("data/ngram=2/M_2.jld", "M_2")
M1forM2 = load("data/ngram=2/M1forM2.jld", "M1forM2")

transition_matrices = tuple(M_2, M1forM2)
