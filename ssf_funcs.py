import numpy as np
def calcmean( a, nans=False):
    if nans:
        m = np.nanmean(a)
    else:
        m = np.mean(a)

    return m

if __name__ == "__main__":
    print('Running tests on calcmean')
    a =np.array((1., 2, 3., np.nan))
    print('input array: ',a)
    print('calcmean(a) = ',calcmean(a))
    print('calcmean(a,nans=True) = ',calcmean(a,nans=True))
