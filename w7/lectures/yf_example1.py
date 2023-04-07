# Downloads Qantas share price beginning 1 January 2020
import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
print(df)
df.to_csv('qan_stk_prc.csv')

