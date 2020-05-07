#!/usr/bin/env python

if __name__ == "__main__":
    import astrology
    astrology.now_cast()

    test_birth = city('Washington')
    astrology.horoscope('Human Bean', test_birth, datetime(2000, 1, 1, 1, 1), 'US/Eastern')
