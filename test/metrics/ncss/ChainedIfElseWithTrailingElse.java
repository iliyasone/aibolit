// Total NCSS = 12

class ChainedIfElse {                           // +1
    public int chainedIfElseMethod(int x) {     // +1
        if(x > 10) {                            // +1
            return 100;                         // +1
        } else if(x > 5) {                      // +1
            return 5;                           // +1
        } else if (x > 0) {                     // +1
            return 1;                           // +1
        } else if (x == 0) {                    // +1
            return 0;                           // +1
        }
        else {                                  // +1
            return -1;                          // +1
        }
    }
}
