import javax.smartcardio.Card;

class CardTest{
    public static void main(String args[]){
        System.out.println("Card.width=" + Card.width);
        System.out.println("Card.height="+Card.height);

        Card c1=new Card();
        c1.kind = "Heart";
        c1.number = 7;

        Card c2= new Card();
        c2.kind= "Spade";
        c2.number=4;

        System.out.println("c1은"+c1.kind +","+c1.number+"이며, 크기는 ("c1.width+","+c1.height+")");
        System.out.println("c2은"+c1.kind +","+c1.number+"이며, 크기는 ("c2.width+","+c2.height+")");

        c1.width =50;
        c1.height = 80;


    }
}

class Card{
    String kind;
    int number;
    static int width = 100;
    static int height = 250;
} // 6-5



class ReturnTest{
    public static void main(String args[]){
        ReturnTest r =new ReturnTest();
        
        int result = r.add(3,5);
        System.out.println(result);
        
        int [] result2 = {0};
        r.add(3,5,result2);
        System.out.println(result2[0]);
        
        int add(int a, int b){
            return a+b;
            
        }
        void add(int a, int b, int [] result){
            result [0] = a+b;
        }
    }
} //6.13
