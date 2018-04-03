import scr.FormatFunctions as Format
import Parameters as P


def print_outcomes(MultipleGameSets, strategy_name):
    """ prints the outcomes of a simulated cohort under steady state
    :param multi_cohort: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of patient survival time
    reward_mean_PI_text = Format.format_estimate_interval(
        estimate=MultipleGameSets.get_mean_total_reward(),
        interval=MultipleGameSets.get_PI_total_reward(alpha=P.ALPHA),
        deci=1)

    # print survival time statistics
    print(strategy_name)
    print(" Estimate of mean rewards for gamblers and {:.{prec}%} prediction interval:".format(1 - P.ALPHA, prec=0),
          reward_mean_PI_text)

def print_comparative_outcomes(GameSets_faircoins,GameSets_unfaircoins):
    increase = GameSets_unfaircoins.get_mean_total_reward()- GameSets_faircoins.get_mean_total_reward()
    percent_increase = -increase/GameSets_faircoins.get_mean_total_reward()
    print("Average increase in rewards for gamblers when using unfair coins:", increase)
    print("the percentage of  average increase in rewards for gamblers when using unfair coins is ", percent_increase*100,"%")

