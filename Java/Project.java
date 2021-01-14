package Project;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;
import java.util.ArrayList;
import java.util.Scanner;

class Food implements Serializable
{
    int item;
    int qty;
    float cost;

    Food(int item,int qty)
    {
        this.item=item;
        this.qty=qty;
        switch(item)
        {
            case 1:cost=qty*50;
                break;
            case 2:cost=qty*200;
                break;
            case 3:cost=qty*30;
                break;
            case 4:cost=qty*100;
                break;
        }
    }
}
class Single implements Serializable
{
    String name;
    String phn;
    String gender;
    ArrayList<Food> food =new ArrayList<>();


    Single()
    {
        this.name="";
    }
    Single(String name,String phn,String gender)
    {
        this.name=name;
        this.phn=phn;
        this.gender=gender;
    }
}
class Double extends Single implements Serializable
{
    String name2;
    String phn2;
    String gender2;

    Double()
    {
        this.name="";
        this.name2="";
    }
    Double(String name,String phn,String gender,String name2,String phn2,String gender2)
    {
        this.name=name;
        this.phn=phn;
        this.gender=gender;
        this.name2=name2;
        this.phn2=phn2;
        this.gender2=gender2;
    }
}
class NotAvailable extends Exception
{
    @Override
    public String toString()
    {
        return "Unavailable !";
    }
}

class holder implements Serializable
{
    Double arr1[]=new Double[10];
    Double arr2[]=new Double[20];
    Single arr3[]=new Single[10];
    Single arr4[]=new Single[20];
}

class Hotel
{
    static holder ob=new holder();
    static Scanner sc = new Scanner(System.in);
    static void CustDetails(int i,int rn)
    {
        String name, phn, gender;
        String name2 = null, phn2 = null;
        String gender2="";
        System.out.print("\nEnter customer name: ");
        name = sc.next();
        System.out.print("Enter phone number: ");
        phn=sc.next();
        System.out.print("Enter gender: ");
        gender = sc.next();
        if(i<3)
        {
            System.out.print("Enter second customer name: ");
            name2 = sc.next();
            System.out.print("Enter phone number: ");
            phn2=sc.next();
            System.out.print("Enter gender: ");
            gender2 = sc.next();
        }

        switch (i) {
            case 1:ob.arr1[rn]=new Double(name,phn,gender,name2,phn2,gender2);
                break;
            case 2:ob.arr2[rn]=new Double(name,phn,gender,name2,phn2,gender2);
                break;
            case 3:ob.arr3[rn]=new Single(name,phn,gender);
                break;
            case 4:ob.arr4[rn]=new Single(name,phn,gender);
                break;
            default:System.out.println("You Have Entered Wrong option");
                break;
        }
    }

    static void bookroom(int i)
    {
        int j;
        int rn;
        System.out.println("\nChoose your room number : ");
        switch (i) {
            case 1:
                for(j=0;j<ob.arr1.length;j++)
                {
                    if(ob.arr1[j]==null)
                    {
                        System.out.print(j+1+",");
                    }
                }
                System.out.print("\nEnter your room number: ");
                try{
                    rn=sc.nextInt();
                    rn--;
                    if(ob.arr1[rn]!=null)
                        throw new NotAvailable();
                    CustDetails(i,rn);
                }
                catch(Exception e)
                {
                    System.out.println("You Have Entered Invalid Option");
                    return;
                }
                break;
            case 2:
                for(j=0;j<ob.arr2.length;j++)
                {
                    if(ob.arr2[j]==null)
                    {
                        System.out.print(j+11+",");
                    }
                }
                System.out.print("\nEnter your room number: ");
                try{
                    rn=sc.nextInt();
                    rn=rn-11;
                    if(ob.arr2[rn]!=null)
                        throw new NotAvailable();
                    CustDetails(i,rn);
                }
                catch(Exception e)
                {
                    System.out.println("You Have Entered Invalid Option");
                    return;
                }
                break;
            case 3:
                for(j=0;j<ob.arr3.length;j++)
                {
                    if(ob.arr3[j]==null)
                    {
                        System.out.print(j+31+",");
                    }
                }
                System.out.print("\nEnter your room number: ");
                try{
                    rn=sc.nextInt();
                    rn=rn-31;
                    if(ob.arr3[rn]!=null)
                        throw new NotAvailable();
                    CustDetails(i,rn);
                }
                catch(Exception e)
                {
                    System.out.println("You Have Entered Invalid Option");
                    return;
                }
                break;
            case 4:
                for(j=0;j<ob.arr4.length;j++)
                {
                    if(ob.arr4[j]==null)
                    {
                        System.out.print(j+41+",");
                    }
                }
                System.out.print("\nEnter your room number: ");
                try{
                    rn=sc.nextInt();
                    rn=rn-41;
                    if(ob.arr4[rn]!=null)
                        throw new NotAvailable();
                    CustDetails(i,rn);
                }
                catch(Exception e)
                {
                    System.out.println("You Have Entered Invalid Option");
                    return;
                }
                break;
            default:
                System.out.println("Please Enter valid option");
                break;
        }
        System.out.println("Room Booked");
    }

    static void features(int i)
    {
        switch (i) {
            case 1:System.out.println("Number of double beds : 1\nAC : Yes\nFree breakfast : Yes\nCharge per day:5000 ");
                break;
            case 2:System.out.println("Number of double beds : 1\nAC : No\nFree breakfast : Yes\nCharge per day:4000  ");
                break;
            case 3:System.out.println("Number of single beds : 1\nAC : Yes\nFree breakfast : Yes\nCharge per day:2500  ");
                break;
            case 4:System.out.println("Number of single beds : 1\nAC : No\nFree breakfast : Yes\nCharge per day:1800 ");
                break;
            default:
                System.out.println("Please Enter valid option");
                break;
        }
    }

    static void availability(int i)
    {
        int j,count=0;
        switch (i) {
            case 1:
                for(j=0;j<10;j++)
                {
                    if(ob.arr1[j]==null)
                        count++;
                }
                break;
            case 2:
                for(j=0;j<ob.arr2.length;j++)
                {
                    if(ob.arr2[j]==null)
                        count++;
                }
                break;
            case 3:
                for(j=0;j<ob.arr3.length;j++)
                {
                    if(ob.arr3[j]==null)
                        count++;
                }
                break;
            case 4:
                for(j=0;j<ob.arr4.length;j++)
                {
                    if(ob.arr4[j]==null)
                        count++;
                }
                break;
            default:
                System.out.println("Please Enter valid option");
                break;
        }
        System.out.println("Available rooms are : "+count);
    }

    static void bill(int rn,int rtype)
    {
        double amount=0;
        String list[]={"Burger","Pizza","Cock","Pasta"};
        System.out.println("\n*******");
        System.out.println(" Bill:-");
        System.out.println("*******");

        switch(rtype)
        {
            case 1:
                amount+=5000;
                System.out.println("\nRoom Charge : "+5000);
                System.out.println("\n===============");
                System.out.println("Food Charges : ");
                System.out.println("===============");
                System.out.println("Item   Quantity    Cost");
                System.out.println("-------------------------");
                for(Food obb:ob.arr1[rn].food)
                {
                    amount+=obb.cost;
                    String format = "%-10s%-10s%-10s%n";
                    System.out.printf(format,list[obb.item-1],obb.qty,obb.cost );
                }

                break;
            case 2:amount+=4000;
                System.out.println("Room Charge : "+4000);
                System.out.println("\nFood Charges : ");
                System.out.println("===============");
                System.out.println("Item   Quantity    Cost");
                System.out.println("-------------------------");
                for(Food obb:ob.arr2[rn].food)
                {
                    amount+=obb.cost;
                    String format = "%-10s%-10s%-10s%n";
                    System.out.printf(format,list[obb.item-1],obb.qty,obb.cost );
                }
                break;
            case 3:amount+=2500;
                System.out.println("Room Charge : "+2500);
                System.out.println("\nFood Charges : ");
                System.out.println("===============");
                System.out.println("Item   Quantity    Cost");
                System.out.println("-------------------------");
                for(Food obb:ob.arr3[rn].food)
                {
                    amount+=obb.cost;
                    String format = "%-10s%-10s%-10s%n";
                    System.out.printf(format,list[obb.item-1],obb.qty,obb.cost );
                }
                break;
            case 4:amount+=1800;
                System.out.println("Room Charge : "+1800);
                System.out.println("\nFood Charges : ");
                System.out.println("===============");
                System.out.println("Item   Quantity    cost");
                System.out.println("-------------------------");
                for(Food obb:ob.arr4[rn].food)
                {
                    amount+=obb.cost;
                    String format = "%-10s%-10s%-10s%n";
                    System.out.printf(format,list[obb.item-1],obb.qty,obb.cost );
                }
                break;
            default:
                System.out.println("Not valid");
        }
        System.out.println("\nTotal Amount : "+amount);
    }

    static void deallocate(int rn,int rtype)
    {
        int j;
        char w;
        switch (rtype) {
            case 1:
                if(ob.arr1[rn]!=null)
                    System.out.println("Room is used by : "+ob.arr1[rn].name);
                else
                {
                    System.out.println("Room is empty already");
                    return;
                }
                System.out.println("Do you want to checkout?(y/n)");
                w=sc.next().charAt(0);
                if(w=='y'||w=='Y')
                {
                    bill(rn,rtype);
                    ob.arr1[rn]=null;
                    System.out.println("Deallocated succesfully");
                }

                break;
            case 2:
                if(ob.arr2[rn]!=null)
                    System.out.println("Room is used by : "+ob.arr2[rn].name);
                else
                {
                    System.out.println("Room is empty already");
                    return;
                }
                System.out.println("Do you want to checkout?(y/n)");
                w=sc.next().charAt(0);
                if(w=='y'||w=='Y')
                {
                    bill(rn,rtype);
                    ob.arr2[rn]=null;
                    System.out.println("Deallocated succesfully");
                }

                break;
            case 3:
                if(ob.arr3[rn]!=null)
                    System.out.println("Room is used by : "+ob.arr3[rn].name);
                else
                {
                    System.out.println("Room is empty already");
                    return;
                }
                System.out.println("Do you want to checkout?(y/n)");
                w=sc.next().charAt(0);
                if(w=='y'||w=='Y')
                {
                    bill(rn,rtype);
                    ob.arr3[rn]=null;
                    System.out.println("Deallocated succesfully");
                }

                break;
            case 4:
                if(ob.arr4[rn]!=null)
                    System.out.println("Room is used by : "+ob.arr4[rn].name);
                else
                {
                    System.out.println("Room is empty already");
                    return;
                }
                System.out.println("Do you want to checkout?(y/n)");
                w=sc.next().charAt(0);
                if(w=='y'||w=='Y')
                {
                    bill(rn,rtype);
                    ob.arr4[rn]=null;
                    System.out.println("Deallocated succesfully");
                }
                break;
            default:
                System.out.println("\nEnter valid option : ");
                break;
        }
    }

    static void order(int rn,int rtype)
    {
        int i,q;
        char wish;
        try{
            System.out.println("\n==========\n   Menu:  \n==========\n\n1.Burger\tRs.50\n2.Pizza\t\tRs.200\n3.Cock\t\tRs.30\n4.Pasta\t\tRs.100\n");
            do
            {
                i = sc.nextInt();
                System.out.print("Quantity : ");
                q=sc.nextInt();

                switch(rtype){
                    case 1: ob.arr1[rn].food.add(new Food(i,q));
                        break;
                    case 2: ob.arr2[rn].food.add(new Food(i,q));
                        break;
                    case 3: ob.arr3[rn].food.add(new Food(i,q));
                        break;
                    case 4: ob.arr4[rn].food.add(new Food(i,q));
                        break;
                }
                System.out.println("Do you want to order anything else?(y/n)");
                wish=sc.next().charAt(0);
            }while(wish=='y'||wish=='Y');
        }
        catch(NullPointerException e)
        {
            System.out.println("\nRoom is not booked");
        }
        catch(Exception e)
        {
            System.out.println("Cannot be done");
        }
    }
}


class write implements Runnable
{
    holder ob;
    write(holder ob)
    {
        this.ob=ob;
    }
    @Override
    public void run() {
        try{
            FileOutputStream fout=new FileOutputStream("backup");
            ObjectOutputStream oos=new ObjectOutputStream(fout);
            oos.writeObject(ob);
        }
        catch(Exception e)
        {
            System.out.println("Error in writing "+e);
        }

    }

}

public class Project {
    public static void main(String[] args){

        try
        {
            File f = new File("backup");
            if(f.exists())
            {
                FileInputStream fin=new FileInputStream(f);
                ObjectInputStream ois=new ObjectInputStream(fin);
                Hotel.ob=(holder)ois.readObject();
            }
            Scanner sc = new Scanner(System.in);
            int ch,ch2;
            char wish;
            x:
            do{

                System.out.println("\nEnter your choice :\n1.Display room details\n2.Display room availability \n3.Book\n4.Order food\n5.Checkout\n6.Exit\n");
                ch = sc.nextInt();
                switch(ch){
                    case 1: System.out.println("\nChoose room type :\n1.Luxury Double Room \n2.Deluxe Double Room \n3.Luxury Single Room \n4.Deluxe Single Room\n");
                        ch2 = sc.nextInt();
                        Hotel.features(ch2);
                        break;
                    case 2:System.out.println("\nChoose room type :\n1.Luxury Double Room \n2.Deluxe Double Room \n3.Luxury Single Room\n4.Deluxe Single Room\n");
                        ch2 = sc.nextInt();
                        Hotel.availability(ch2);
                        break;
                    case 3:System.out.println("\nChoose room type :\n1.Luxury Double Room \n2.Deluxe Double Room \n3.Luxury Single Room\n4.Deluxe Single Room\n");
                        ch2 = sc.nextInt();
                        Hotel.bookroom(ch2);
                        break;
                    case 4:
                        System.out.print("Room Number : ");
                        ch2 = sc.nextInt();
                        if(ch2>60)
                            System.out.println("Room does not exist");
                        else if(ch2>40)
                            Hotel.order(ch2-41,4);
                        else if(ch2>30)
                            Hotel.order(ch2-31,3);
                        else if(ch2>10)
                            Hotel.order(ch2-11,2);
                        else if(ch2>0)
                            Hotel.order(ch2-1,1);
                        else
                            System.out.println("Room does not exist");
                        break;
                    case 5:
                        System.out.print("Room Number : ");
                        ch2 = sc.nextInt();
                        if(ch2>60)
                            System.out.println("Room does not exist");
                        else if(ch2>40)
                            Hotel.deallocate(ch2-41,4);
                        else if(ch2>30)
                            Hotel.deallocate(ch2-31,3);
                        else if(ch2>10)
                            Hotel.deallocate(ch2-11,2);
                        else if(ch2>0)
                            Hotel.deallocate(ch2-1,1);
                        else
                            System.out.println("Room does not exist");
                        break;
                    case 6:break x;

                }

                System.out.println("\nDo you want to continue?(y/n)");
                wish=sc.next().charAt(0);
                if(!(wish=='y'||wish=='Y'||wish=='n'||wish=='N'))
                {
                    System.out.println("You Have Entered Invalid Option");
                    System.out.println("\nDo you want to continue?(y/n)");
                    wish=sc.next().charAt(0);
                }

            }while(wish=='y'||wish=='Y');

            Thread t=new Thread(new write(Hotel.ob));
            t.start();
        }
        catch(Exception e)
        {
            System.out.println("Not a valid input");
        }
    }
}
