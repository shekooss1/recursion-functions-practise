def count_down(x):
    if x == 1 :
        print(x)
        print("Done!")
        return 

    else :
         print(x)
         count_down(x-1)

count_down(4)

def recursive_sum(x):
 
    if x==0 :
       return 0
    else :
       return x + recursive_sum(x-1)

print(recursive_sum(5))

def sum_digits(x):
    if x == 0 :
        return 0
    else :
        return (x%10) + sum_digits(x//10)


print(sum_digits(1234))


def reverse_string(s):
    x = len(s) -1
    if len(s) == 0 :
        return s 

    else :
        return s[x] + reverse_string(s[:-1])

print(reverse_string("abcd"))

def is_palindrome(s) :
     if len(s) <=1 :
         return True
     if s[0] != s[-1]:
        return False

     return is_palindrome(s[1:-1])



print(is_palindrome("aba"))


def list_sum(l) :
    if len(l) == 0 :
        return 0

    else :
        return l[-1] + list_sum(l[:-1])


print(list_sum([1,2,34]))


def count_occ(l,x,i=0,j=0):
    if i == len(l) :
        return j
    if l[i] == x :
        j+=1

    i+=1
    return count_occ(l,x,i,j)

print(count_occ([1, 2, 2, 3, 2], 2))
print(count_occ([4,5,6], 1))


def is_sorted(l,i=0):
    if i == len(l) - 1:
        return True
    
    if len(l) <= 1 :
        return True
     

    if l[i] > l[i+1]:
      return False
    
    i+=1
    return is_sorted(l,i)   

print(is_sorted([-1,1,2,3,4]))

def binary_search( left, right,nums = list,target=int) :
     nums=nums
     if left > right:
        return -1
     middle = (left+right) // 2

     
     if nums[middle] == target :
        return middle         
     if nums[middle] > target :
        return binary_search(left,middle-1,nums,target)
     if nums[middle] < target :
      return binary_search(middle+1,right,nums,target)

print(binary_search(0,len([1,2,3,4])-1,[1,2,3,4],5))


def fibbonaci(n) :
    if n ==0:
        return 0
    if n==1:
        return 1
    
    else :
        return fibbonaci(n-1) + fibbonaci(n-2)


print(fibbonaci(5)) 

def recursive_power(x,n) :
    if n== 0 :
        return 1
    if n ==1 :
        return x

    else :
        return x * recursive_power(x,n-1)

print(recursive_power(3,3))

def count_digits_recursively(x,i=0):
    if x==0 and i==0 :
           return i+1
    if x==0 :
       return i
        
    return count_digits_recursively(x//10,i+1)


print(count_digits_recursively(0))

def reverse_int(n,i=0):
  if n == 0:
   return i
  else :     
   i = (i*10) + n%10
   

   return reverse_int(n//10,i)


r = reverse_int(123)
print(r)

def recursive_max(n,i=0,max=0):
    if i == len(n) :
        return max

    remaining_max = recursive_max(n, i + 1, max)

    if n[i] > remaining_max :
        return n[i]
    else :
         return remaining_max    

max = recursive_max([-3,-4,-2])
print(max)

def factorial(n):
    if n ==1 or n==0 :
        return 1 
    else :
        return n * factorial(n-1)


print(factorial(5))

def flatten_lists(l):
    flat_list = []

    for item in l:
        if isinstance(item, list):
            flat_list.extend(flatten_lists(item))
        else:
            flat_list.append(item)

    return flat_list

print(flatten_lists([1,2,3,[1,2,[12,34]],[45,67]]))
