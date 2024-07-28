import java.io.*;
import java.util.Scanner;

class Property {
    String loc;
    int id;
    int price;
    int area;
    String swim;
    String gard;

    public Property() {
        loc = "";
        id = 0;
        price = 0;
        area = 0;
        swim = "";
        gard = "";
    }
}

public class Main {
    static Property p1 = new Property();
    static File file1 = new File("file1.txt");
    static Property[] arr = new Property[30];
    static Property[] arr1 = new Property[20];
    static Property[] arr2 = new Property[20];
    static Property[] arr3 = new Property[20];

    static Scanner scanner = new Scanner(System.in);

    public static void add() {
        try {
            FileWriter writer = new FileWriter(file1, true);
            char no = 'y';
            int x = 1;

            while (no == 'y') {
                System.out.print("Enter the location of the property: ");
                p1.loc = scanner.nextLine();
                System.out.print("Enter the id: ");
                p1.id = scanner.nextInt();
                scanner.nextLine();
                System.out.print("Enter the price: ");
                p1.price = scanner.nextInt();
                scanner.nextLine();
                System.out.print("Enter the area (acres): ");
                p1.area = scanner.nextInt();
                scanner.nextLine();
                System.out.print("Swimming pool available (Yes/No): ");
                p1.swim = scanner.nextLine();
                System.out.print("Garden available (Yes/No): ");
                p1.gard = scanner.nextLine();

                writer.write(p1.loc + "\n" + p1.id + "\n" + p1.price + "\n" + p1.area + "\n" + p1.swim + "\n" + p1.gard + "\n\n");
                System.out.print("\nTO ADD MORE? (y/n): ");
                no = scanner.nextLine().charAt(0);
            }

            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void display() {
        try {
            Scanner reader = new Scanner(file1);
            int x = 0;
            int count = 0;
    
            for (int i = 0; i < 20; i++) {
                arr1[i] = new Property();
            }
    
            System.out.println("\n        *********************************");
            System.out.println("         !!!!   AVAILABLE PROPERTY   !!!!");
            System.out.println("        *********************************\n");
    
            while (reader.hasNextLine() && x < 20) {
                arr1[x].loc = reader.nextLine();
    
                if (!reader.hasNextLine()) break;
                String idString = reader.nextLine();
                if (idString.matches("-?\\d+")) {
                    arr1[x].id = Integer.parseInt(idString);
                }
    
                if (!reader.hasNextLine()) break;
                String priceString = reader.nextLine();
                if (priceString.matches("-?\\d+")) {
                    arr1[x].price = Integer.parseInt(priceString);
                }
    
                if (!reader.hasNextLine()) break;
                String areaString = reader.nextLine();
                if (areaString.matches("-?\\d+")) {
                    arr1[x].area = Integer.parseInt(areaString);
                }
    
                if (!reader.hasNextLine()) break;
                arr1[x].swim = reader.nextLine();
    
                if (!reader.hasNextLine()) break;
                arr1[x].gard = reader.nextLine();
    
                x++;
            }
    
            for (int i = 0; i < x; i++) {
                if (arr1[i].id != 0 || arr1[i].price != 0) {
                    System.out.println("\n!!!   DETAILS OF " + (i + 1) + " PROPERTY   !!!");
                    System.out.println("\nLOCATION----> " + arr1[i].loc);
                    System.out.println("ID----> " + arr1[i].id);
                    System.out.println("PRICE----> " + arr1[i].price);
                    System.out.println("AREA(acre's)----> " + arr1[i].area);
                    System.out.println("SWIMMING POOL----> " + arr1[i].swim);
                    System.out.println("GARDEN----> " + arr1[i].gard + "\n");
                    count = 1;
                }
            }
    
            reader.close();
    
            if (count == 0) {
                System.out.println("               !!!   NULL   !!!");
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void sold() {
        try {
            File soldFile = new File("sold.txt");
            Scanner reader = new Scanner(soldFile);
            int x = 0;
            int count = 0;
    
            for (int i = 0; i < 20; i++) {
                arr1[i] = new Property();
            }
    
            System.out.println("\n        *********************************");
            System.out.println("         !!!!   SOLD OUT PROPERTY   !!!!");
            System.out.println("        *********************************\n");
    
            while (reader.hasNextLine() && x < 20) {
                arr1[x].loc = reader.nextLine();
    
                if (!reader.hasNextLine()) break;
                String idString = reader.nextLine();
                if (idString.matches("-?\\d+")) {
                    arr1[x].id = Integer.parseInt(idString);
                }
    
                if (!reader.hasNextLine()) break;
                String priceString = reader.nextLine();
                if (priceString.matches("-?\\d+")) {
                    arr1[x].price = Integer.parseInt(priceString);
                }
    
                if (!reader.hasNextLine()) break;
                String areaString = reader.nextLine();
                if (areaString.matches("-?\\d+")) {
                    arr1[x].area = Integer.parseInt(areaString);
                }
    
                if (!reader.hasNextLine()) break;
                arr1[x].swim = reader.nextLine();
    
                if (!reader.hasNextLine()) break;
                arr1[x].gard = reader.nextLine();
    
                x++;
            }
    
            for (int i = 0; i < x; i++) {
                if (arr1[i].id != 0 || arr1[i].price != 0) {
                    System.out.println("\n!!!   DETAILS OF " + (i + 1) + " PROPERTY   !!!");
                    System.out.println("\nLOCATION----> " + arr1[i].loc);
                    System.out.println("ID----> " + arr1[i].id);
                    System.out.println("PRICE----> " + arr1[i].price);
                    System.out.println("AREA(acre's)----> " + arr1[i].area);
                    System.out.println("SWIMMING POOL----> " + arr1[i].swim);
                    System.out.println("GARDEN----> " + arr1[i].gard + "\n");
                    count = 1;
                }
            }
    
            reader.close();
    
            if (count == 0) {
                System.out.println("               !!!   NULL   !!!");
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
    
    public static void search() {
        try {
            Scanner scanner = new Scanner(System.in);
    
            int budget, x = 0;
            int acre, choice;
    
            System.out.println("\n1>>Enter 1 to search through area");
            System.out.println("2>>Enter 2 to search through price");
            System.out.print("Enter your choice: ");
            choice = scanner.nextInt();
            scanner.nextLine(); 
    
            for (int i = 0; i < 30; i++) {
                arr[i] = new Property();
            }
    
            File inputFile = new File("file1.txt");
            Scanner reader = new Scanner(inputFile);
    
            while (reader.hasNextLine() && x < 30) {
                arr[x].loc = reader.nextLine();
    
                if (!reader.hasNextLine()) break;
                String idString = reader.nextLine();
                if (idString.matches("-?\\d+")) {
                    arr[x].id = Integer.parseInt(idString);
                }
    
                if (!reader.hasNextLine()) break;
                String priceString = reader.nextLine();
                if (priceString.matches("-?\\d+")) {
                    arr[x].price = Integer.parseInt(priceString);
                }
    
                if (!reader.hasNextLine()) break;
                String areaString = reader.nextLine();
                if (areaString.matches("-?\\d+")) {
                    arr[x].area = Integer.parseInt(areaString);
                }
    
                if (!reader.hasNextLine()) break;
                arr[x].swim = reader.nextLine();
    
                if (!reader.hasNextLine()) break;
                arr[x].gard = reader.nextLine();
    
                x++;
            }
    
            reader.close();
    
            int hj = 0;
            int count = 0;
    
            switch (choice) {
                case 1:
                    System.out.print("Enter your Desired area: ");
                    acre = scanner.nextInt();
                    scanner.nextLine(); 
    
                    System.out.println("\n        *********************************");
                    System.out.println("         !!!!   AVAILABLE PROPERTY   !!!!");
                    System.out.println("        *********************************\n");
    
                    for (int i = 0; i < 30; i++) {
                        if (acre == arr[i].area || (acre > arr[i].area && arr[i].price != 0)) {
                            System.out.println("\n!!!   DETAILS OF " + (i + 1) + " PROPERTY   !!!");
                            System.out.println("\nLOCATION----> " + arr[i].loc);
                            System.out.println("ID----> " + arr[i].id);
                            System.out.println("PRICE----> " + arr[i].price);
                            System.out.println("AREA(acre's)----> " + arr[i].area);
                            System.out.println("SWIMMING POOL----> " + arr[i].swim);
                            System.out.println("GARDEN----> " + arr[i].gard + "\n");
                            hj = 1;
                        }
                    }
                    break;
    
                case 2:
                    System.out.print("Enter your budget: ");
                    budget = scanner.nextInt();
                    scanner.nextLine(); // Consume the newline character
    
                    System.out.println("\n        *********************************");
                    System.out.println("         !!!!   AVAILABLE PROPERTY   !!!!");
                    System.out.println("        *********************************\n");
    
                    for (int i = 0; i < 30; i++) {
                        if (budget == arr[i].price || (arr[i].price < budget && arr[i].price != 0)) {
                            System.out.println("\n!!!   DETAILS OF " + (i + 1) + " PROPERTY   !!!");
                            System.out.println("\nLOCATION----> " + arr[i].loc);
                            System.out.println("ID----> " + arr[i].id);
                            System.out.println("PRICE----> " + arr[i].price);
                            System.out.println("AREA(acre's)----> " + arr[i].area);
                            System.out.println("SWIMMING POOL----> " + arr[i].swim);
                            System.out.println("GARDEN----> " + arr[i].gard + "\n");
                            hj = 1;
                        }
                    }
                    break;
    
                default:
                    System.out.println("\n!!!   Enter a Valid Option   !!!");
                    hj = 1;
                    break;
            }
    
            if (hj == 0) {
                System.out.println("\n!!!   NOT FOUND   !!!");
            }
    
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
    
    public static void edit() {
        try {
            Scanner scanner = new Scanner(System.in);
    
            int sim, x = 0;
            String ch = "y";
            int z, price1;
            String ary;
            int gj = 0;
    
            File inputFile = new File("file1.txt");
            Scanner reader = new Scanner(inputFile);
    
            for (int i = 0; i < 20; i++) {
                arr1[i] = new Property();
            }
    
            while (reader.hasNextLine() && x < 20) {
                arr1[x].loc = reader.nextLine();
    
                if (!reader.hasNextLine()) break;
                String idString = reader.nextLine();
                if (idString.matches("-?\\d+")) {
                    arr1[x].id = Integer.parseInt(idString);
                }
    
                if (!reader.hasNextLine()) break;
                String priceString = reader.nextLine();
                if (priceString.matches("-?\\d+")) {
                    arr1[x].price = Integer.parseInt(priceString);
                }
    
                if (!reader.hasNextLine()) break;
                String areaString = reader.nextLine();
                if (areaString.matches("-?\\d+")) {
                    arr1[x].area = Integer.parseInt(areaString);
                }
    
                if (!reader.hasNextLine()) break;
                arr1[x].swim = reader.nextLine();
    
                if (!reader.hasNextLine()) break;
                arr1[x].gard = reader.nextLine();
    
                x++;
            }
    
            reader.close();
    
            while (ch.equals("y")) {
                System.out.print("Enter the id of the property you want to edit: ");
                sim = scanner.nextInt();
                scanner.nextLine(); 
    
                for (int i = 0; i < 20; i++) {
                    if (sim == arr1[i].id) {
                        System.out.println("Press 1 to change location");
                        System.out.println("Press 2 to change price");
                        System.out.print("Enter your choice: ");
                        z = scanner.nextInt();
                        scanner.nextLine(); 
    
                        switch (z) {
                            case 1:
                                System.out.print("Enter the location: ");
                                ary = scanner.nextLine();
                                arr1[i].loc = ary;
                                System.out.println("\n!!!  SUCCESSFULLY CHANGED  !!!\n");
                                break;
    
                            case 2:
                                System.out.print("Enter the price: ");
                                price1 = scanner.nextInt();
                                scanner.nextLine(); 
                                arr1[i].price = price1;
                                System.out.println("\n!!!  SUCCESSFULLY CHANGED  !!!\n");
                                break;
    
                            default:
                                System.out.println("Enter a valid choice");
                        }
                        gj = 1;
                    }
                }
    
                if (gj == 0) {
                    System.out.println("\n!!!   NOT FOUND   !!!");
                }
                gj = 0;
    
                System.out.print("\nTO EDIT MORE? (y/n): ");
                ch = scanner.nextLine();
            }
    
            PrintWriter writer = new PrintWriter("file1.txt");
            int j = 0;
            while (j < 20 && arr1[j].price != 0) {
                writer.println(arr1[j].loc);
                writer.println(arr1[j].id);
                writer.println(arr1[j].price);
                writer.println(arr1[j].area);
                writer.println(arr1[j].swim);
                writer.println(arr1[j].gard);
                j++;
            }
            writer.close();
    
            for (int w = 0; w < 20; w++) {
                arr1[w].id = 0;
                arr1[w].price = 0;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    public static void delete() {
        try {
            Scanner scanner = new Scanner(System.in);
    
            int sim, x = 0;
            String ch = "y";
            String ary;
            int k = 0;
    
            File inputFile = new File("file1.txt");
            Scanner reader = new Scanner(inputFile);
    
            for (int i = 0; i < 20; i++) {
                arr2[i] = new Property();
            }
    
            while (reader.hasNextLine() && x < 20) {
                arr2[x].loc = reader.nextLine();
    
                if (!reader.hasNextLine()) break;
                String idString = reader.nextLine();
                if (idString.matches("-?\\d+")) {
                    arr2[x].id = Integer.parseInt(idString);
                }
    
                if (!reader.hasNextLine()) break;
                String priceString = reader.nextLine();
                if (priceString.matches("-?\\d+")) {
                    arr2[x].price = Integer.parseInt(priceString);
                }
    
                if (!reader.hasNextLine()) break;
                String areaString = reader.nextLine();
                if (areaString.matches("-?\\d+")) {
                    arr2[x].area = Integer.parseInt(areaString);
                }
    
                if (!reader.hasNextLine()) break;
                arr2[x].swim = reader.nextLine();
    
                if (!reader.hasNextLine()) break;
                arr2[x].gard = reader.nextLine();
    
                x++;
            }
    
            reader.close();
    
            while (ch.equals("y")) {
                System.out.print("Enter the id of the property you want to delete: ");
                sim = scanner.nextInt();
                scanner.nextLine(); 
    
                for (int i = 0; i < 20; i++) {
                    if (sim == arr2[i].id) {
                        arr2[i].price = 0;
                        arr2[i].id = 0;
                        k = 1;
                        System.out.println("\n!!!  SUCCESSFULLY DELETED  !!!\n");
                    }
                }
    
                if (k == 0) {
                    System.out.println("\n!!!   NOT FOUND   !!!");
                    break;
                }
                scanner.nextLine(); 
                System.out.print("\nTO DELETE MORE? (y/n): ");
                ch = scanner.nextLine();
            }
    
            PrintWriter writer = new PrintWriter("file1.txt");
            for (int j = 0; j < 20; j++) {
                if (arr2[j].price != 0) {
                    writer.println(arr2[j].loc);
                    writer.println(arr2[j].id);
                    writer.println(arr2[j].price);
                    writer.println(arr2[j].area);
                    writer.println(arr2[j].swim);
                    writer.println(arr2[j].gard);
                }
            }
            writer.close();
    
            for (int w = 0; w < 20; w++) {
                arr2[w].id = 0;
                arr2[w].price = 0;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    public static void buy() {
        try {
            Scanner scanner = new Scanner(System.in);
    
            File inputFile = new File("file1.txt");
            Scanner reader = new Scanner(inputFile);
            int x = 0;
            int sim;
            int pay;
            int gj = 0;
    
            for (int i = 0; i < 20; i++) {
                arr3[i] = new Property();
            }
    
            while (reader.hasNextLine() && x < 20) {
                arr3[x].loc = reader.nextLine();
    
                if (!reader.hasNextLine()) break;
                String idString = reader.nextLine();
                if (idString.matches("-?\\d+")) {
                    arr3[x].id = Integer.parseInt(idString);
                }
    
                if (!reader.hasNextLine()) break;
                String priceString = reader.nextLine();
                if (priceString.matches("-?\\d+")) {
                    arr3[x].price = Integer.parseInt(priceString);
                }
    
                if (!reader.hasNextLine()) break;
                String areaString = reader.nextLine();
                if (areaString.matches("-?\\d+")) {
                    arr3[x].area = Integer.parseInt(areaString);
                }
    
                if (!reader.hasNextLine()) break;
                arr3[x].swim = reader.nextLine();
    
                if (!reader.hasNextLine()) break;
                arr3[x].gard = reader.nextLine();
    
                x++;
            }
    
            reader.close();
    
            PrintWriter writer = new PrintWriter("file1.txt");
    
            System.out.print("Enter the ID of the property you want to buy: ");
            sim = scanner.nextInt();
            scanner.nextLine(); 
    
            for (int i = 0; i < 20; i++) {
                if (arr3[i].id == sim) {
                    System.out.println("Price of this property is: " + arr3[i].price);
                    System.out.print("Pay your amount: ");
                    pay = scanner.nextInt();
                    scanner.nextLine(); 
    
                    if (pay == arr3[i].price) {
                        System.out.println("\n\n!!!   PAYMENT SUCCESSFUL   !!!");
                        System.out.println("!!!     PURCHASED      !!!");
                        gj = 1;
                        arr3[i].id = 0;
                        arr3[i].price = 0;
                    } else if (pay > arr3[i].price) {
                        System.out.println("\n\n!!!   WE ARE NOT CORRUPTED   !!!");
                    } else if (pay < arr3[i].price) {
                        System.out.println("\n\n!!!   PAYMENT DECLINED   !!!");
                    }
                }
            }
    
            if (gj == 0) {
                System.out.println("\n\n!!!   NOT FOUND   !!!");
            }
    
            for (int i = 0; i < 20; i++) {
                if (arr3[i].price != 0 || arr3[i].id != 0) {
                    writer.println(arr3[i].loc);
                    writer.println(arr3[i].id);
                    writer.println(arr3[i].price);
                    writer.println(arr3[i].area);
                    writer.println(arr3[i].swim);
                    writer.println(arr3[i].gard);
                }
            }
            writer.close();
    
            for (int v = 0; v < 20; v++) {
                arr3[v].id = 0;
                arr3[v].price = 0;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    
    public static void fullFledgedSearch() {
        Scanner scanner = new Scanner(System.in);
    
        System.out.print("Enter Your budget: ");
        int budget = scanner.nextInt();
        scanner.nextLine(); 
    
        System.out.print("Enter Your Area: ");
        int area = scanner.nextInt();
        scanner.nextLine(); 
    
        System.out.print("Enter (Yes/No) for Swimming Pool: ");
        String swim1 = scanner.nextLine();
    
        System.out.print("Enter (Yes/No) for Garden: ");
        String gard1 = scanner.nextLine();
    
        for (int i = 0; i < 20; i++) {
            arr3[i] = new Property();
        }
    
        try {
            File inputFile = new File("file1.txt");
            Scanner reader = new Scanner(inputFile);
            int x = 0;
    
            while (reader.hasNextLine() && x < 20) {
                arr3[x].loc = reader.nextLine();
                arr3[x].id = Integer.parseInt(reader.nextLine());
                arr3[x].price = Integer.parseInt(reader.nextLine());
                arr3[x].area = Integer.parseInt(reader.nextLine());
                arr3[x].swim = reader.nextLine();
                arr3[x].gard = reader.nextLine();
    
                x++;
            }
            reader.close();
    
            int count = 0;
    
            System.out.println("\n        *********************************");
            System.out.println("         !!!!   AVAILABLE PROPERTY   !!!!");
            System.out.println("        *********************************\n");
    
            for (int i = 0; i < x; i++) {
                if (arr3[i].price <= budget &&
                    arr3[i].area <= area &&
                    arr3[i].swim.equalsIgnoreCase(swim1) &&
                    arr3[i].gard.equalsIgnoreCase(gard1) &&
                    arr3[i].price != 0) {
                    System.out.println("\n!!!   DETAILS OF " + (i + 1) + " PROPERTY   !!!");
                    System.out.println("\nLOCATION----> " + arr3[i].loc);
                    System.out.println("ID----> " + arr3[i].id);
                    System.out.println("PRICE----> " + arr3[i].price);
                    System.out.println("AREA(acre's)----> " + arr3[i].area);
                    System.out.println("SWIMMING POOL----> " + arr3[i].swim);
                    System.out.println("GARDEN----> " + arr3[i].gard + "\n");
                    count = 1;
                }
            }
    
            if (count == 0) {
                System.out.println("           !!!   NOT FOUND   !!!");
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        int option;
        System.out.println("\n        *********************************");
        System.out.println("         !!!!   HEY! USER WELCOME   !!!!");
        System.out.println("        *********************************");

        while (true) {
            System.out.println("\n\nEnter option 1 for adding any property");
            System.out.println("Enter option 2 to display the property");
            System.out.println("Enter option 3 to display the sold property");
            System.out.println("Enter option 4 to search");
            System.out.println("Enter option 5 to edit the property");
            System.out.println("Enter option 6 to delete the property");
            System.out.println("Enter option 7 to buy a property");
            System.out.println("Enter option 8 for full-fledged search");
            System.out.println("Enter option 9 to exit the program");
            System.out.print("\nEnter your option: ");

            option = scanner.nextInt();
            scanner.nextLine();

            switch (option) {
                case 1:
                    add();
                    break;
                case 2:
                    display();
                    break;
                case 3:
                    sold();
                    break;    
                case 4:
                    search();
                    break;
                case 5:
                    edit();
                    break;
                case 6:
                    delete();
                    break;
                case 7:
                    buy();
                    break;
                case 8:
                    fullFledgedSearch();
                    break;
                case 9:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Enter a valid option!");
            }
        }
    }
}
