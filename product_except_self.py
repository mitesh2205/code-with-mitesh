def product_except_self(nums):
    n = len(nums)
    prefix = [1] * n 
    postfix = [1] * n
    product = [1] * n

    for i in range(1,n):
        prefix[i] = nums[i-1] * prefix[i-1]
    for i in rangge(n-1,-1,-1):
        postfix[i] = nums[i+1] * postfix[i+1]

    for i in range(n):
        product[i] = prefix[i] * postfix[i]

    return product

    # bruteforce way

    # product = [1] * n

    # for i in range(n):
    #     for j in range(n):
    #         if i != j:
    #             product[i] *= nums[j]
    # return product