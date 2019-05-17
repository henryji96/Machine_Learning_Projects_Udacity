#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """
    residual_error=net_worths-predictions
    residual_error_abs=map(abs,residual_error)
    data_zip=zip(ages,net_worths,residual_error_abs)
    data_sort=sorted(data_zip,key=lambda x: x[2],reverse=True)

    rmNum=int(0.1*len(predictions))
    cleaned_data=data_sort[rmNum:]

    ### your code goes here


    return cleaned_data
