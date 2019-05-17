import pandas as pd
import os
def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))
########################################################################
def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)# 1create empty df for designated date
    
    if 'SPY' not in symbols:  # 2add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp=pd.read_csv(symbol_to_path(symbol, base_dir="data"), # 3read in data from the symbol
                           index_col='Date',
                           parse_dates=True,
                           usecols=['Date','Adj Close'],
                           na_values=['nan'])
        df_temp=df_temp.rename(columns={'Adj Close':symbol})       # 4rename the adjust close column to the symbol name
        df=df.join(df_temp) 
        if symbol =='SPY':#5drop rows where SPY is na/ensure SPY is used as a reference-we don't have na values in the spy column
            df=df.dropna(subset=['SPY'])
    return df
########################################################################
def normalize_data(df):
    return df/df.iloc[0,:]
########################################################################
def plot_selected(df, columns, start_index, end_index):
    """Plot the desired columns over index values in the given range."""
    # TODO: Your code here
    # Note: DO NOT modify anything else!
    plot_data(df.loc[start_index:end_index,columns],title='Selected data')

def plot_data(df, title="Stock prices"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()
########################################################################
def get_bollinger_bands(rm,rstd):
    upper_band=rm+2*rstd
    lower_band=rm-2*rstd
    return upper_band,lower_band

def get_rolling_mean(values, window):
    """Return rolling mean of given values, using specified window size."""
    return values.rolling( window=window,center=False).mean()


def get_rolling_std(values, window):
    """Return rolling standard deviation of given values, using specified window size."""
    # TODO: Compute and return rolling standard deviation
    return values.rolling(window=window,center=False).std()
########################################################################
def compute_daily_returns(df):
    """Compute and return the daily return values."""
    # TODO: Your code here
    # Note: Returned DataFrame must have the same number of rows
    daily_returns=df.copy()
    daily_returns[1:]=(df[1:]/df[:-1].values)-1
    daily_returns.iloc[0]=0
    return daily_returns
    #return daily_returns[1:]
########################################################################
def fill_missing_values(df_data):
    df_data.fillna(method='ffill',inplace=True)#fill forward
    df_data.fillna(method='bfill',inplace=True)#fill backward
########################################################################
def compute_daily_portfolio_values(dates,symbols,allocs,initial_capital):
    df=get_data(symbols,dates)
    normed=normalize_data(df)
    alloced=normed*allocs
    pos_vals=alloced*initial_capital
    port_val=pos_vals.sum(axis=1)
    return port_val
########################################################################
"""1.cumulative return 2.average daily return 3.risk-std of daily return 4.sharpe ratio"""
def compute_portfolio_statistics(port_val,frequency,annual_daily_rf_bank=0.1):
    port_rets=compute_daily_returns(port_val)[1:]
    
    cum_ret=(port_val[-1]/port_val[0]-1)#1
    avg_daily_ret=port_rets.mean()#2
    std_daily_ret=port_rets.std()#3
    #4 
    if frequency=='daily':
        K=252**(1.0/2)
    elif frequency=='weekly':
        K=52**(1.0/2)
    elif frequency=='monthly':
        K=12**(1.0/2)
        
    daily_rf=(1+annual_daily_rf_bank)**(1.0/252)-1  
    sharp_ratio=K*(avg_daily_ret-daily_rf)/std_daily_ret
    
    return cum_ret,avg_daily_ret,std_daily_ret,sharp_ratio