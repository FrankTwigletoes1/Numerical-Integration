"""
procedure Integration(f, a, b, n)
    h := (b - a) / n
    sum1 := f(a + h/2)
    sum2 := 0

    loop på i fra 1 til (n - 1)
        sum1 = sum1 + f(a + h * i + h/2)
        sum2 = sum2 + f(a + h * i)
"""