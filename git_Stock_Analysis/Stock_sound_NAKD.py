from yahoo_fin import stock_info as si
import winsound

frequency = 2500  
ticker = 'NAKD'
ticker2 = 'SNDL'
low_threshhold = 1.50
upper_threshhold = 2.0
while True:
    price = float(si.get_live_price(ticker))
    price2 = float(si.get_live_price(ticker2))
    print ("NAKD:", price)
    print ("SNDL", price2)
    if price <= low_threshhold:
         duration = 1000  # Set Duration To 1000 ms == 1 second
         winsound.Beep(frequency, duration)
         continue
    elif price >= upper_threshhold:
         duration = 100
         for i in range(10):
            winsound.Beep(frequency, duration)
         continue
    else:
        continue

    
