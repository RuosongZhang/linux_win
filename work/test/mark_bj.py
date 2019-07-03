
def mark_bj(mark1,mark2,mark3,mark4,mark5):
    mark=mark1+mark2+mark3+mark4+mark5
    if mark == 11111:
        print('it is a GW trigger: initial, tiles, early, real')
        obs_priority_plus = 2
    elif mark == 11121:
        print('it is a GW trigger: initial, tiles, late, real')
        obs_priority_plus = 0
    elif mark == 12111:
        print('it is a GW trigger: Update, tiles, early, real')
        obs_priority_plus = 3
    elif mark == 12121:
        print('it is a GW trigger: Update, tiles, late, real')
        obs_priority_plus = 1

    elif mark == 11112:
        print('it is a GW trigger: initial, tiles, early, test')
        obs_priority_plus = 2
    elif mark == 11122:
        print('it is a GW trigger: initial, tiles, late, test')
        obs_priority_plus = 0
    elif mark == 12112:
        print('it is a GW trigger: Update, tiles, early, test')
        obs_priority_plus = 3
    elif mark == 12122:
        print('it is a GW trigger: Update, tiles, late, test')
        obs_priority_plus = 1

    elif mark == 11211:
        print('it is a GW trigger: initial, galaxies, early, real')
        obs_priority_plus = 2
    elif mark == 11221:
        print('it is a GW trigger: initial, galaxies, late, real')
        obs_priority_plus = 0
    elif mark == 12211:
        print('it is a GW trigger: Update, galaxies, early, real')
        obs_priority_plus = 3
    elif mark == 12221:
        print('it is a GW trigger: Update, galaxies, late, real')
        obs_priority_plus = 1

    elif mark == 11212:
        print('it is a GW trigger: initial, galaxies, early, test')
        obs_priority_plus = 2
    elif mark == 11222:
        print('it is a GW trigger: initial, galaxies, late, test')
        obs_priority_plus = 0
    elif mark == 12212:
        print('it is a GW trigger: Update, galaxies, early, test')
        obs_priority_plus = 3
    elif mark == 12222:
        print('it is a GW trigger: Update, galaxies, late, test')
        obs_priority_plus = 1


    elif mark == 11132:
        print('it is a GW trigger: initial, tiles, late, test')
        obs_priority_plus = 0
    elif mark == 11131:
        print('it is a GW trigger: initial, tiles, late, real')
        obs_priority_plus = 0
    elif mark == 11232:
        print('it is a GW trigger: initial, galaxies, late, test')
        obs_priority_plus = 0
    elif mark == 11231:
        print('it is a GW trigger: initial, galaxies, late, real')
        obs_priority_plus = 0
    elif mark == 12131:
        print('it is a GW trigger: Update, tiles, late, real')
        obs_priority_plus = 1
    elif mark == 12231:
        print('it is a GW trigger: Update, galaxies, late, real')
        obs_priority_plus = 1
    elif mark == 12232:
        print('it is a GW trigger: Update, galaxies, late, test')
        obs_priority_plus = 1
    elif mark == 12132:
        print('it is a GW trigger: Update, tiles, late, test')
        obs_priority_plus = 1

    elif mark == 21111:
        print('it is a Fermi GRB trigger: initial, tiles, early, real')
        obs_priority_plus = 3
    elif mark == 21121:
        print('it is a Fermi GRB trigger: initial, tiles, late, real')
        obs_priority_plus = 3
    elif mark == 22111:
        print('it is a Fermi GRB trigger: Update, tiles, early, real')
        obs_priority_plus = 4
    elif mark == 22121:
        print('it is a Fermi GRB trigger: Update, tiles, late, real')
        obs_priority_plus = 4

    elif mark == 21112:
        print('it is a Fermi GRB trigger: initial, tiles, early, test')
        obs_priority_plus = 3
    elif mark == 21122:
        print('it is a Fermi GRB trigger: initial, tiles, late, test')
        obs_priority_plus = 3
    elif mark == 22112:
        print('it is a Fermi GRB trigger: Update, tiles, early, test')
        obs_priority_plus = 4
    elif mark == 22122:
        print('it is a Fermi GRB trigger: Update, tiles, late, test')
        obs_priority_plus = 4

    elif mark == 21211:
        print('it is a Fermi GRB trigger: initial, galaxies, early, real')
        obs_priority_plus = 3
    elif mark == 21221:
        print('it is a Fermi GRB trigger: initial, galaxies, late, real')
        obs_priority_plus = 3
    elif mark == 22211:
        print('it is a Fermi GRB trigger: Update, galaxies, early, real')
        obs_priority_plus = 4
    elif mark == 22221:
        print('it is a Fermi GRB trigger: Update, galaxies, late, real')
        obs_priority_plus = 4

    elif mark == 21212:
        print('it is a Fermi GRB trigger: initial, galaxies, early, test')
        obs_priority_plus = 3
    elif mark == 21222:
        print('it is a Fermi GRB trigger: initial, galaxies, late, test')
        obs_priority_plus = 3
    elif mark == 22212:
        print('it is a Fermi GRB trigger: Update, galaxies, early, test')
        obs_priority_plus = 4
    elif mark == 22222:
        print('it is a Fermi GRB trigger: Update, galaxies, late, test')
        obs_priority_plus = 4


    elif mark == 21132:
        print('it is a Fermi GRB trigger: initial, tiles, late, test')
        obs_priority_plus = 3
    elif mark == 21131:
        print('it is a Fermi GRB trigger: initial, tiles, late, real')
        obs_priority_plus = 3
    elif mark == 21232:
        print('it is a Fermi GRB trigger: initial, galaxies, late, test')
        obs_priority_plus = 0
    elif mark == 21231:
        print('it is a Fermi GRB trigger: initial, galaxies, late, real')
        obs_priority_plus = 0
    elif mark == 22131:
        print('it is a Fermi GRB trigger: Update, tiles, late, real')
        obs_priority_plus = 2
    elif mark == 22231:
        print('it is a Fermi GRB trigger: Update, galaxies, late, real')
        obs_priority_plus = 2
    elif mark == 22232:
        print('it is a Fermi GRB trigger: Update, galaxies, late, test')
        obs_priority_plus = 2
    elif mark == 22132:
        print('it is a Fermi GRB trigger: Update, tiles, late, test')
        obs_priority_plus = 2

    elif mark == 31311:
        print('it is a Swift GRB trigger: initial, early, real')
        obs_priority_plus = 9
    elif mark == 31321:
        print('it is a Swift GRB trigger: initial, middle, real')
        obs_priority_plus = 8
    elif mark == 31331:
        print('it is a Swift GRB trigger: initial, late, real')
        obs_priority_plus = 6
    elif mark == 32311:
        print('it is a Swift GRB trigger: Update, early, real')
        obs_priority_plus = 9
    elif mark == 32321:
        print('it is a Swift GRB trigger: Update, middle, real')
        obs_priority_plus = 8
    elif mark == 32331:
        print('it is a Swift GRB trigger: Update, late, real')
        obs_priority_plus = 6

    elif mark == 31312:
        print('it is a Swift GRB trigger: initial, early, test')
        obs_priority_plus = 9
    elif mark == 31322:
        print('it is a Swift GRB trigger: initial, middle, test')
        obs_priority_plus = 8
    elif mark == 31332:
        print('it is a Swift GRB trigger: initial, late, test')
        obs_priority_plus = 6
    elif mark == 32312:
        print('it is a Swift GRB trigger: Update, early, test')
        obs_priority_plus = 9
    elif mark == 32322:
        print('it is a Swift GRB trigger: Update, middle, test')
        obs_priority_plus = 8
    elif mark == 32332:
        print('it is a Swift GRB trigger: Update, late, test')
        obs_priority_plus = 6

    elif mark == 41311:
        print('it is a Neutrino trigger: initial, early, real')
        obs_priority_plus = 0
    elif mark == 41321:
        print('it is a Neutrino trigger: initial, middle, real')
        obs_priority_plus = 0
    elif mark == 41331:
        print('it is a Neutrino trigger: initial, late, real')
        obs_priority_plus = 0
    elif mark == 42311:
        print('it is a Neutrino trigger: Update, early, real')
        obs_priority_plus = 0
    elif mark == 42321:
        print('it is a Neutrino trigger: Update, middle, real')
        obs_priority_plus = 0
    elif mark == 42331:
        print('it is a Neutrino trigger: Update, late, real')
        obs_priority_plus = 0

    elif mark == 41312:
        print('it is a Neutrino trigger: initial, early, test')
        obs_priority_plus = 0
    elif mark == 41322:
        print('it is a Neutrino trigger: initial, middle, test')
        obs_priority_plus = 0
    elif mark == 41332:
        print('it is a Neutrino trigger: initial, late, test')
        obs_priority_plus = 0
    elif mark == 42312:
        print('it is a Neutrino trigger: Update, early, test')
        obs_priority_plus = 0
    elif mark == 42322:
        print('it is a Neutrino trigger: Update, middle, test')
        obs_priority_plus = 0
    elif mark == 42332:
        print('it is a Neutrino trigger: Update, late, test')
        obs_priority_plus = 0
    return obs_priority_plus
