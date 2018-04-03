import scr.FormatFunctions as Format
import scr.StatisticalClasses as Stat
import Parameters as P


def print_outcomes(sim_output, coins):
    """ prints the outcomes of a simulated cohort under steady state
    :param sim_output: output of a simulated cohort
    :param strategy_name: the name of the selected therapy
    """

    # mean and confidence interval text of game rewards
    reward_mean_CI_text = Format.format_estimate_interval(
        estimate=sim_output.get_ave_reward(),
        interval=sim_output.get_CI_reward(alpha=P.ALPHA),
        deci=1)

    # print casino owners rewards statistics
    print(coins)
    print("  Estimate of mean rewards for casino owners and {:.{prec}%} confidence interval:".format(1 - P.ALPHA, prec=0),
          reward_mean_CI_text)

def print_comparative_outcomes(sim_output_fair_coins, sim_output_unfair_coins):
    """ prints expected and percentage increase in survival time when drug is available
    :param sim_output_no_drug: output of a cohort simulated when drug is not available
    :param sim_output_with_drug: output of a cohort simulated when drug is available
    """

    # increase in rewards
    increase = Stat.DifferenceStatIndp(
        name='Increase in survival time',
        x=sim_output_unfair_coins.get_rewards(),
        y_ref=sim_output_fair_coins.get_rewards()
    )
    # estimate and CI
    estimate_CI = Format.format_estimate_interval(
        estimate=increase.get_mean(),
        interval=increase.get_t_CI(alpha=P.ALPHA),
        deci=1
    )
    print("Average increase in rewards for casino owners and {:.{prec}%} confidence interval"
          " when using unfair coins:".format(1 - P.ALPHA, prec=0),
          estimate_CI)

    # % increase in rewards
    relative_diff = Stat.RelativeDifferenceIndp(
        name='Average % increase in survival time',
        x=sim_output_unfair_coins.get_rewards(),
        y_ref=sim_output_fair_coins.get_rewards()
    )
    # estimate and CI
    estimate_CI2 = Format.format_estimate_interval(
        estimate=-relative_diff.get_mean(),
        interval=-relative_diff.get_bootstrap_CI(alpha=P.ALPHA, num_samples=1000),
        deci=1,
        form=Format.FormatNumber.PERCENTAGE
    )
    print("Average percentage of increase rewards for casino owners  and {:.{prec}%} confidence interval"
          " when using unfair coins:".format(1 - P.ALPHA, prec=0),
          estimate_CI2)
