import scipy.stats
import sys
class ci2nstd:
    def __init__(self) :
        return
    
    def t_dist(self, ci, dof, ntail=2):
        if ntail != 1 and ntail != 2 :
            print "ntail can only be 1 or 2 "
            sys.exit('')
        else:
            self.alpha=1.-ci/100.
            self.nstd=scipy.stats.t.ppf(1.0-(self.alpha/ntail),dof)
            self.dof=dof
            self.ntail=ntail
        return self.nstd