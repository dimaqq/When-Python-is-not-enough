float stepx(float r, float x, int cnt)
{
    while (cnt--)
        x = r * x * (1 - x);
    return x;
}
