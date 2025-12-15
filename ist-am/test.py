import re

latex_code = r"""
\toprule
Variable & Importance in percent\\
\midrule
Net.Income.to.Stockholder.s.Equity & 8.132\\
Net.worth.Assets & 4.336\\
Equity.to.Liability & 3.935\\
Net.Value.Per.Share..C.  & 3.787\\
Retained.Earnings.to.Total.Assets & 3.659\\
\addlinespace
Current.Liability.to.Equity & 3.581\\
Degree.of.Financial.Leverage..DFL. & 3.181\\
Working.Capital.Equity &  3.105\\
Interest.Expense.Ratio &3.050\\
Interest.Coverage.Ratio..Interest.expense.to.EBIT. & 2.994\\
\addlinespace
Non.industry.income.and.expenditure.revenue &  2.897\\
After.tax.net.Interest.Rate &2.827\\
Total.income.Total.expense & 2.775\\
Current.Liability.to.Current.Assets & 2.695\\
Working.Capital.to.Total.Assets & 2.587\\
\addlinespace
Total.expense.Assets & 2.515\\
Cash.Total.Assets &  2.222\\
Inventory.Working.Capital &  1.999\\
Current.Liability.to.Assets & 1.976\\
Operating.profit.per.person & 1.903\\
\addlinespace
No.credit.Interval &  1.888\\
Realized.Sales.Gross.Margin & 1.794\\
Equity.to.Long.term.Liability &  1.659\\
Working.capitcal.Turnover.Rate & 1.656\\
Inventory.and.accounts.receivable.Net.value & 1.610\\
\addlinespace
Total.Asset.Return.Growth.Rate.Ratio & 1.581\\
Continuous.Net.Profit.Growth.Rate & 1.483\\
Cash.Reinvestment..  & 1.437\\
Operating.Profit.Per.Share..Yuan... & 1.387\\
Cash.Flow.to.Liability  & 1.377\\
\addlinespace
Cash.Flow.to.Equity &  1.368\\
Cash.flow.rate & 1.341\\
Net.Worth.Turnover.Rate..times. & 1.320\\
Total.Asset.Turnover & 1.317\\
Cash.Flow.to.Total.Assets & 1.315\\
\addlinespace
Long.term.fund.suitability.ratio..A. & 1.315\\
Cash.Flow.to.Sales  & 1.308\\
Cash.Flow.Per.Share & 1.242\\
Operating.Profit.Rate& 1.212\\
Current.Assets.Total.Assets & 1.196\\
\addlinespace
Quick.Assets.Total.Assets &  1.151\\
Operating.Profit.Growth.Rate &  1.124\\
Current.Liability.to.Liability & 1.118\\
Realized.Sales.Gross.Profit.Growth.Rate & 1.096\\
Regular.Net.Profit.Growth.Rate & 1.041\\
\addlinespace
Contingent.liabilities.Net.worth & 0.898\\
tax\_rate\_A & 0.583\\
Liability.Assets.Flag &  0.026\\
"""

def replace_dots_in_variable_names(latex_text):
    def repl(match):
        variable = match.group(1).replace('.', ' ')
        rest = match.group(2)
        return f"{variable}{rest}"

    # Match "variable & value \\"
    pattern = re.compile(r"^(.*?)(&.*\\\\)$", re.MULTILINE)
    return pattern.sub(repl, latex_text)

updated_latex = replace_dots_in_variable_names(latex_code)
print(updated_latex)
