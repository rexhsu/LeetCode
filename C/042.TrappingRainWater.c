#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))

int trap(int* height, int heightSize){
    int ans = 0;
    int *l = malloc(sizeof(int) * heightSize);
    int *r = malloc(sizeof(int) * heightSize);
    
    for (int i=0; i<heightSize; i++)
        l[i] = i == 0 ? height[i] : MAX(l[i-1], height[i]);
    for (int i=heightSize-1; i>=0; i--)
        r[i] = i == (heightSize -1) ? height[i] : MAX(r[i+1], height[i]);
    for (int i=0; i<heightSize; i++)
        ans += MIN(l[i], r[i]) - height[i];
    free(l);
    free(r);
    return ans;
}
