import Parameters as P
import Classes as Cls
import SupportTransientState as Support

# create Gamesets for gamblers when the coin is fair
Gamesets_faircoins = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS),
    prob_head =P.FAIR_PROB_HEAD,
    n_games_in_a_set = P.REAL_POP_SIZE
)

# simulate all cohorts
Gamesets_faircoins.simulation()

# create Gamesets for gamblers when the coin is unfair
Gamesets_unfaircoins = Cls.MultipleGameSets(
    ids=range(P.NUM_SIM_COHORTS),
    prob_head =P.UNFAIR_PROB_HEAD,
    n_games_in_a_set = P.REAL_POP_SIZE
)

# simulate all cohorts
Gamesets_unfaircoins.simulation()

#print outcomes for fair coins
Support.print_outcomes(Gamesets_faircoins,"fair coins")

#print outcomes for unfair coins
Support.print_outcomes(Gamesets_unfaircoins,"unfair coins")

#print comparative outcomes
Support.print_comparative_outcomes(Gamesets_faircoins,Gamesets_unfaircoins)