package com.fsjava;
import java.awt.*;
import java.text.NumberFormat;
import java.util.Arrays;
import java.util.Date;
import java.util.Locale;
import java.util.Scanner;

// class
public class Main {
    // method
    public static void start(){
        // print hello world
        System.out.println("Hello World!");
        // variable int : Primitive : storing simple values
        int age = 21;
        // variable int : Reference : for storing complex objects
        int myAge = age + 1;
        System.out.println(myAge);

        // PRIMITIVE VARIABLES
        byte myNewAge = 30;
        // use underscore as 123,456,789 as 123 thousand
        long viewCount = 123_456_789L;
        // double or float
        float price = 10.99F;
        // char one character
        char letter = 'A';
        // boolean
        boolean isEligible = false;

        // REFERENCE VARIABLES
        Date today = new Date();
        System.out.println(today);

        // store memory number so when point1 changes point2 changes
        Point point1 = new Point(1, 1);
        Point point2 = point1;
        point1.x = 2;
        System.out.println(point2);

        // not using point
        int u = 1;
        int p = u;
        u = 2;
        System.out.println(p);

        // strings manipulation
        String message = "Hello World" + "!!";
        System.out.println(message.endsWith("!"));
        System.out.println(message.startsWith("!"));
        System.out.println(message.length());
        System.out.println(message.indexOf("W"));
        System.out.println(message.indexOf("Lol"));
        // fix the spaces
        System.out.println(message.trim());
        System.out.println(message.replace("W", "D"));
        System.out.println(message.toUpperCase(Locale.ROOT));
        System.out.println(message.toLowerCase(Locale.ROOT));

        // use special characters
        String newMessage = "\t Hello \n \"Atom\"";
        String path = "c:\\Windows\\...";
        System.out.println(newMessage);
        System.out.println(path);

        // Arrays
        // how many items we want in array
        int [] numbers = new int[5];
        numbers[0] = 1;
        numbers[1] = 2;
        numbers[2] = 3;
        numbers[2] = 3;
        numbers[3] = 4;
        numbers[4] = 5;
        // calculated from the address
        System.out.println(numbers);
        // to print it
        System.out.println(Arrays.toString(numbers));

        //another way
        int [] collection = {5,4,3,1,2,10};
        Arrays.sort(collection);
        System.out.println(Arrays.toString(collection));
        System.out.println(collection.length);

        // multi-Dimensional Arrays
        // or { {1,2,3},{4.5.6} }
        int [][] mdNumbers = new int[2][3];
        mdNumbers[0][0] = 1;
        mdNumbers[1][1] = 2;
        System.out.println(Arrays.toString(mdNumbers));
        System.out.println(Arrays.deepToString(mdNumbers));

        // constant : final variables cannot be changed
        final float PI = 3.14F;
        // we get an error
        // PI = 2;
        System.out.println(PI);


        // Arithmetic operation
        int n1 = 10 + 3;
        int n2 = n1 - 3;
        System.out.println(n2);
        double n3 = (double)n2 /(double)3;
        int n4 = (int)n3 * 10;
        System.out.println(n3);
        System.out.println(n4);

        int n5 = 1;
        int n6 = n5++;
        int n7 = ++n5;
        n6 += 2;
        n6 -= 5;
        System.out.println(n5);
        System.out.println(n6);
        System.out.println(n7);



        // casting

        // automatic conversion : IMPLICIT
        // byte > short > int > long > float > double
        short x = 1;
        // x is short then converted
        int y = x + 4;
        System.out.println(y);

        //  manual : Explicit
        double a = 1.1;
        // have to convert it to double
        double b = a + 4;
        int z = (int)a + 2;
        System.out.println(b);
        System.out.println(z);

        // str to int
        String e = "1";
        int newE = Integer.parseInt(e);
        System.out.println(newE + 10);
        String d = "1.1";
        double newD = Double.parseDouble(d);
        System.out.println(newD + 10);

        // math Class

        // Ceil
        double result = Math.ceil(1.1F);
        System.out.println(result);

        // FLOOR
        double result2 = Math.floor(1.2F);
        System.out.println(result2);

        // round
        System.out.println(Math.round(newD));

        // max returns the max number
        System.out.println(Math.max(1,2));

        // random default between 0 and 1
        double randX = Math.random();
        // explicit its not automatic
        int randY = (int) Math.round(randX* 100);
        System.out.println(randX);
        System.out.println(randY);

        // formatting a number

        NumberFormat currency = NumberFormat.getCurrencyInstance();
        String rc = currency.format(1234567.891);
        System.out.println(rc);

        NumberFormat percentage = NumberFormat.getPercentInstance();
        String rp = percentage.format(0.15);
        System.out.println(rp);

        // method chaining
        System.out.println(NumberFormat.getPercentInstance().format(0.26));


        // reading inputs from terminal
        Scanner scanner = new Scanner(System.in);
        System.out.print("Age: ");
        byte userAge = scanner.nextByte();
        System.out.print("Name: ");
        String userName = scanner.next().trim();
        String userFName = scanner.nextLine();
        System.out.println(userFName);
        System.out.println(userName + userFName+ " is " + userAge + " Years old");

    }
    public static void calculator(){
        final byte MONTHS_IN_YEAR = 12;
        final byte PERCENT= 100;
        Scanner scanner = new Scanner(System.in);

        System.out.print("Principle: ");
        int principle = scanner.nextInt();

        System.out.print("Annual interest rate: ");
        float annualInterest = scanner.nextFloat();
        float monthlyInterest = annualInterest / PERCENT / MONTHS_IN_YEAR;

        System.out.print("Period(Years): ");
        byte years = scanner.nextByte();
        int number_payments = years * MONTHS_IN_YEAR;

        double mortgage = principle * (monthlyInterest * Math.pow(1 + monthlyInterest, number_payments) / Math.pow(1+monthlyInterest, number_payments) - 1);
        String mortgageFormatted = NumberFormat.getCurrencyInstance().format(mortgage);
        System.out.println("Mortgage: " + mortgageFormatted);

    }
    public static void Flow(){
        System.out.println("Comparison");
        int x = 1;
        int y = 1;
        int z = 2;
        System.out.println(x == y);
        System.out.println(x == z);
        System.out.println(x >= y);
        System.out.println(x != z);

        System.out.println("Logical");
        int temperature = 22;
        // and
        boolean isWarm =  temperature > 20 && temperature < 30;
        System.out.println(isWarm);

        boolean hasHighIncome = false;
        boolean hasGoodCredit = true;
        boolean hasCriminalRecord = false;
        // or + not operator !
        boolean isEligible = (hasHighIncome || hasGoodCredit) && !hasCriminalRecord;
        System.out.println(isEligible);

        // if statement
        Scanner scanner = new Scanner(System.in);
        System.out.print("Temperature: ");
        int temp = scanner.nextInt();

        if(temp > 30) {
            System.out.println("Hot, Drink water!");
        } else if (temp > 20 && temp <= 30){
            System.out.println("warm");
        } else{
            System.out.println("cold day");
        }

        // better if statement
        int income = 120_000;
        boolean hasHighIIncome = (income > 100_000);
        System.out.println(hasHighIIncome);

        // ternary operator
        // different classes based on income
        String className = income > 100_000 ? "First" : "Economy";
        System.out.println(className);


        // switch statement
        String role = "moderator";

        switch (role) {
            case "admin":
                System.out.println("Admin role");
                break;
            case "moderator":
                System.out.println("Moderator role");
                break;
            default:
                System.out.println("Guest role");
        }












    }
    public static void FizzBuzz(){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Number: ");
        int numb = scanner.nextInt();

        if (numb % 5 == 0 && numb % 3 == 0){
            System.out.println("FizzBuzz");
        }
        else if (numb % 3 == 0){
            System.out.println("Buzz");
        }
        else if (numb % 5 == 0){
            System.out.println("FizzBuzz");
        }
        else{
            System.out.println(numb);
        }

    }
    public static void main(String[] args){
        // start();
        // calculator();
        // Flow()
        FizzBuzz();

    }
}
