func myPow(x float64, n int) float64 {
    if n < 0 {
        return myPow(1/x, -n)
    } else if n == 0 {
        return float64(1.0)
    } else if n == 1{
        return x
    } else if n % 2 == 0{
        return myPow(x*x, n/2)
    } else {
        return x*myPow(x, n-1)
    }
}
