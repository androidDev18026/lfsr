## LSFR

![LFSR example](https://www.researchgate.net/profile/Muhammad-Osama-2/publication/292130031/figure/fig5/AS:668783521828901@1536461825862/An-example-of-a-7-bit-LFSR.ppm)

**Linear Feedback Shift Generator**

---

Implementing core code for a random number generator as shown in [Youtube Video](https://www.youtube.com/watch?v=Ks1pw1X22y4)

```
usage: Linear Shift State Register [-h] -n N -i I [--log-level {info,warn,error}]

Generate random numbers

optional arguments:
  -h, --help            show this help message and exit
  -n N, --bits N        initial number
  -i I, --iterations I  number of random bits to generate
  --log-level {info,warn,error}
                        set log level
```

Example ***`python3 lfsr.py -n 9 -i 50 --log-level warn`***
