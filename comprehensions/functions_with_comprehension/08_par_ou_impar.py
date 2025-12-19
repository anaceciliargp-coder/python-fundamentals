def par_ou_impar(values):
    return ["par" if v % 2 == 0 else "impar" for v in values]

nums = [1, 2, 3, 4, 5, 6]
print(par_ou_impar(nums))
