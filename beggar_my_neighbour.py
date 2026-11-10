
def main() -> None:
    count : int = 0
    countT : int = 0
    pl1 : list[int] = [4,7,14,8,13,3,12,10,6,4,8,6,5,7,12,11,7,10,10,6,9,11,5,3,2,6]
    pl2 : list[int] = [7,9,4,9,5,13,13,2,13,14,9,2,14,3,3,11,11,8,4,2,8,12,5,10,14,12]
    l1 : list[int] = []
    l2 : list[int] = []
    itm1 : int
    itm2 : int

    while len(pl1) != 52 or len(pl2) != 52:
        itm1 = pl1.pop(0)
        itm2 = pl2.pop(0)
        count += 1

        if itm1 != itm2:
            if itm1 > itm2:
                pl1.extend(l1)
                pl1.append(itm1)
                pl1.extend(l2)
                pl1.append(itm2)
                print("\n",pl1,"\n",pl2,"\n")
            else:
                pl2.extend(l2)
                pl2.append(itm2)
                pl2.extend(l1)
                pl2.append(itm1)
                print("\n",pl1,"\n",pl2,"\n")
            l1.clear()
            l2.clear()
        else:
            while itm1 == itm2:
                countT += 1
                l1.append(itm1)
                l2.append(itm2)
                if len(pl1) < 4 and len(pl2) < 4:
                    print("Draw :",count,countT)
                    exit()
                elif len(pl1) < 4:
                    print("Player 2 wins :",count,countT)
                    exit()
                elif len(pl2) < 4:
                    print("Player 1 wins :",count,countT)
                    exit()
                l1.extend(pl1[0:3])
                del pl1[0:3]
                l2.extend(pl2[0:3])
                del pl2[0:3]
                itm1 = pl1.pop(0)
                itm2 = pl2.pop(0)
    else:
        if len(pl1) == 52:
            print("Player 1 wins :", count,countT)
        else:
            print("Player 2 wins :",count,countT)
        exit()

if __name__ == '__main__':
    main()
