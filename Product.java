class Product{
    static int count = 0;
    int serialNo;
    {
        ++count;
        serialNo=count;
    }
}
class ProductTest{
    public static void main(String args[]){
        Product p1= new Product();
        Product p2= new Product();
        Product p3= new Product();
        
        System.out.println("p1의 제품번호는"+p1.serialNo);
        System.out.println("p1의 제품번호는"+p1.serialNo);
        System.out.println("p1의 제품번호는"+p1.serialNo);
    }
}//6-29
