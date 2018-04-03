import Parameters as P
import Classes as Cls
import SupportSteadyState as Support

# create a set of games of casino owners with fair coins
cohortFaircoins = Cls.SetOfGames(
    id = 1,
    prob_head=P.FAIR_PROB_HEAD,
    n_games=P.SIM_POP_SIZE
)
# simulate the cohort
outcomes_fair = cohortFaircoins.simulation()

# create a set of games of casino owners without fair coins
cohortUnfaircoins = Cls.SetOfGames(
    id = 2,
    prob_head=P.UNFAIR_PROB_HEAD,
    n_games=P.SIM_POP_SIZE
)
# simulate the cohort
outcomes_unfair = cohortUnfaircoins.simulation()

#print comparatie results
Support.print_comparative_outcomes(cohortFaircoins,cohortUnfaircoins)

#print outcomes for fair coins
Support.print_outcomes(outcomes_fair,"FairCoins")

#print outcomes for unfair coins
Support.print_outcomes(outcomes_unfair,"UnfairCoins")