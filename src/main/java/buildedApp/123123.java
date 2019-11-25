

static  int n = 25;
static double k = 0, i = 5, N = 416;
static double x = 0, y = 0, e = 0.001, lambda = 10000;
public static double f(double x, double y) {
    return Math.pow(x + i, 2) + Math.pow(y + i/2, 2) - (x * y) / N;
}
public static double fx(double x, double y) {
    return 2 * (x + i) - y / N;
}
public static double fy(double x, double y) {
    return 2 * (y + i/2) - x / N;
}

public static double f2xx(double x, double y) {
    return 2;
}
public static double f2xy(double x, double y) {
    return 1;
}
public static double f2yx(double x, double y) {
    return 1;
}

public static double f2yy(double x, double y) {
    return 2;
}
public static double vectorModule(double x, double y){
    return Math.sqrt(x*x + y*y);
}

public static void main(String[] args) {
    int z = 0;
    while (vectorModule(fx(x, y), fy(x, y)) > e){
        if (k > n){break;}
        double[] s = s(x, y);
        if (f(x, y) > f(x + s[0], y + s[1])){
            x += s[0];
            y += s[1];
            lambda = 1/(2 * lambda);
            k++;
        } else {
            lambda = 2 * lambda;
        }
        System.out.printf("%d: ‖∇f(x, y))‖ = %f; x = %f, y = %f; f(x, y) = %f\n", ++z, vectorModule(fx(x, y), fy(x, y)), x, y, f(x, y));
    }

    System.out.println("x = " + x + " y = " + y + " f(x, y) = " + f(x, y));
}
