def sample_evolution(initial_parameters):
    """
    Evolves the system by simulating many sample paths
    """
    # unpack list
    num_of_steps                = initial_parameters[0]
    num_of_records              = initial_parameters[1]
    num_of_states               = initial_parameters[2]
    num_of_samples              = initial_parameters[3]
    transition_matrix           = initial_parameters[4]
    initial_distribution_matrix = initial_parameters[5]

    ### -------------- set stage for simulation -------------- ###
    # create empirical probability distribution function
    epdf    = np.zeros([num_of_records, num_of_states], dtype = float)
    # initial the epdf by writing the initial distribution matrix to epdf
    epdf[0] = initial_distribution_matrix[:]
    #printltx(r"initialized epdf = " + ltxmtx(epdf))

    scaled_initial_distribution_matrix = np.rint(initial_distribution_matrix*num_of_samples).astype(int)
    simulation_ledger                  = np.zeros([num_of_records, num_of_samples], dtype = int)

    # initialize simulation ledger by distributing probabilities
    # from the initial distribution matrix to the sample population
    simulation_ledger_index_1 = 0
    for state_index in range(num_of_states):
        simulation_ledger_index_2 = simulation_ledger_index_1 + scaled_initial_distribution_matrix[state_index]
        simulation_ledger[0, simulation_ledger_index_1:simulation_ledger_index_2] = state_index
        simulation_ledger_index_1 = simulation_ledger_index_2
    # shuffle the columns in the first row
    np.random.shuffle(simulation_ledger[0])

    ### -------------- run the simulation -------------- ###
    absorption_states = [6, 8]
    # vector to record how many steps until first return to an absorption state
    first_return_absorption = np.zeros(num_of_samples, dtype = int)
    for step in range(num_of_steps):
        # "step" here refers to the location with respect to the number of records
        # since we're looping through the same array
        current_step = step % num_of_records
        next_step    = (step + 1) % num_of_records
        for sample in range(num_of_samples):
            current_state      = simulation_ledger[current_step, sample]
            # choose random number between 0 and 1
            random_probability = np.random.rand()
            # randomly decide which state sample goes to next
            for next_state in range(num_of_states):
                random_probability -= transition_matrix[current_state, next_state]
                if random_probability < 0:
                    simulation_ledger[next_step, sample] = next_state
                    if next_state not in absorption_states:
                        first_return_absorption[sample] += 1
                    break
        epdf[next_step, :] = np.histogram(simulation_ledger[next_step, :], \
                                          normed = True, bins = range(num_of_states + 1))[0]

    average_absorption_time = np.sum(first_return_absorption) / num_of_samples
    printltx(r"Average absorption time is " + str(average_absorption_time))
    plt.title('Distribution of Absorption Times')
    plt.hist(first_return_absorption, bins = range(np.max(first_return_absorption)))
    plt.xlabel('jumps')
    plt.ylabel('frequency')
    plt.show()

    # right now, the last distribution is not necessarily on the bottom of the epdf matrix;
    # so, the following code rearranges the rows of the matrix to make sure the final distribution is on bottom
    epdf = np.roll(epdf, num_of_records - next_step - 1, axis = 0)
    return epdf