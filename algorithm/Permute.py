def permute(step, n, k, arrOfIndex, checked, mapOfShrine):
    if (step == k):
        # do something

    else:
        for i in range(n):
            if checked[i] == False:
                arrOfIndex[step] = i
                checked[i] = True
                permute(step + 1, n, k, arrOfIndex, checked, mapOfShrine)
                checked[i] = False