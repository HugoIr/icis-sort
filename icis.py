def icis_sort(arr):
    m = len(arr) # Size of the array 
    min = med = max = 0
    a = [0] * m

    for index in range(m):
        x = arr[index]

        if (index == 0):
            a[0] = x
            continue

        if ( x>= a[max] and max < m-1):
            max += 1
            a[max] = x
            med = int(max/2)

        #Compare x with the minimum-value in the array minimum-value is usually a [0].
        elif (x <= a[min]):
            if (max < m-1):
                max += 1

            # shift data from min to max
            for p in range(max, 0, -1):
                a[p] = a[p-1]
            
            # insert x into the array
            a[0] = x

            # recalculate the med
            med = int(max/2)


        # Check x between the minimum-value and the medium-value in the array    
        elif ( x>a[min] and x < a[med]):
            if (max < m-1):
                max += 1
            for L in range (1, med+1):
                if (x <= a[L]):
                    # shift data
                    for p in range (max, L, -1):
                        a[p] = a[p-1]

                a[L] = x
                med = int(max/2)
                break

        # Check x between the medium-value and the maximum-value in the array.
        elif (x >= a[med] and a[max]):
            if (max < m-1):
                max += 1
            for L in range (med, max+1):
                if (x <= a[L]):
                    for p in range (max, L, -1):
                        a[p] = a[p-1]

                    a[L] = x
                    med = int(max/2)
                    medium = a[med]
                    break

    return a

# For print the result
ar = [3,2,5,9,7]
print(icis_sort(ar))
