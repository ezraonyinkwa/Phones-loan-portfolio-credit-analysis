#---------Portfolio Health-----------
#1 PAR Rate
par_30 = credit[credit['days_past_due'] >= 30]['balance'].sum()
par_60 = credit[credit['days_past_due']>=60]['balance'].sum()
par_90 = credit[credit['days_past_due']>=90]['balance'].sum()

print(f"Portfolio at Risk (PAR) - 30 days: KES {par_30:,}")
print(f"Portfolio at Risk (PAR) - 60 days: KES {par_60:,}")
print(f"Portfolio at Risk (PAR) - 90 days: KES {par_90:,}") 

# 2.Impaired Rate
#Impaired Rate
credit["impaired_flag"] = credit["days_past_due"] > 0

#Define denominator for impaired rate calculation
active = credit[credit["balance"] > 0]

impaired = active[active["days_past_due"] > 0]

impaired_rate = impaired["balance"].sum() / active["balance"].sum()

# 3.Average Arrears per Impaired Account
avg_arrears = impaired["balance"].sum() / impaired.shape[0] if impaired.shape[0] > 0 else 0
print(f"Average Arrears per Impaired Account: KES {avg_arrears:,.2f}")



#Credit Outcomes × Customer Experience


#
