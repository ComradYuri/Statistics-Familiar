import familiar
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

# import life expectancy of vein pack users. Then use 1 sample T-test to check for significance on a mean population
# life expectancy of 71.
vein_pack_lifespans = familiar.lifespans(package='vein')
vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)
print(vein_pack_test.pvalue)
if vein_pack_test.pvalue < .05:
    print("The Vein Pack Is Proven To Make You Live Longer!")
else:
    print('The Vein Pack Is Probably Good For You Somehow')

# Test if there is difference between 'artery' and 'vein' package with two sample T test.
artery_pack_lifespans = familiar.lifespans(package='artery')
package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
if package_comparison_results.pvalue < .05:
    print("the Artery Package guarantees even stronger results!")
else:
    print("the Artery Package is also a great product!")

# Discrete test for iron levels: low, medium, high. Chi squared is used to test for difference between vein and artery
iron_contingency_table = familiar.iron_counts_for_package()
print(iron_contingency_table)
iron_pvalue = chi2_contingency(iron_contingency_table)[1]
print(iron_pvalue)
_, iron_pvalue, _, _ = chi2_contingency(iron_contingency_table)
print(iron_pvalue)
if iron_pvalue < .05:
    print("The Artery Package Is Proven To Make You Healthier!")
else:
    print("While We Can't Say The Artery Package Will Help You, I Bet It's Nice!")
