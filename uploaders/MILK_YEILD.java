import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.sql.*;
import java.text.DecimalFormat;
import java.text.SimpleDateFormat;
import java.util.ArrayList;

public class MILK_YEILD {
    static final String DB_URL = "";
    static final String USER = "";
    static final String PASS = "";
    private static DecimalFormat format = new DecimalFormat("#.#");
    private static ArrayList<String> data = new ArrayList<>();


    private static final String DAMHEAD = "EAR_TAG,LACT_NO,MILK_DATE,FEED_GROUP,Yield_1,PeakFlow_1,Duration_1,StallPosition_1,RealTime_1,Yield_2,PeakFlow_2,Duration_2,StallPosition_2,RealTime_2,Yield_3,PeakFlow_3,Duration_3,StallPosition_3,RealTime_3,Dail Yld,MILK_DATE_MON,MILK_DATE_TUE,MILK_DATE_WED,MILK_DATE_THU,MILK_DATE_FRI";


    public static void main(String[] args) {
        readfile("cleanData/MILK_YIELDwith0.csv", DAMHEAD);
        System.out.println(data);
        // Open a connection
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected to DB...");

            insertData(conn);


            //Statement stmt = conn.createStatement();
            //String test = "INSERT INTO dam VALUES (1, 1, 1, 1, 1, 1, 1, 1, 1, 11/11/11, 1, 1)";
            //stmt.executeUpdate(test);

            //stmt = conn.createStatement();
            //String sql = "SELECT * from langhillherd.dam";
            //ResultSet set = stmt.executeQuery(sql);
            //printResults(set);
        } catch (Exception e) {
            e.printStackTrace();
       }
    }

    /**
     * Reads in the file and stores it into a static array of Data.
     * @param writefilename
     * @throws SQLException
     */
    private static void readfile(String writefilename, String validator) {
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new FileReader(writefilename));
            String line = "";
            // Reads the first line.
            line = reader.readLine();
            // Checks to see if the file is empty, if it is, terminates the program.
            // If the file is not empty, it checks to see if it is in the correct format to be processed, if it is not, then the program terminates.
            //if (!line.equals(validator)) {
                //System.out.println("This file is not in the correct format to be used.");
                //System.out.println("First line is " + line);
                //System.exit(0);
            //}
            // Reads the file and stores the data in a static ArrayList to put the values into the program.
            while ((line = reader.readLine()) != null) {
                data.add(line);
            }
        } catch (FileNotFoundException e) {
            System.out.println("File not found: " + e.getMessage());
            System.exit(0);
        } catch (IOException e) {
            System.out.println("IO Exception: " + e.getMessage());
            System.exit(0);
        } finally {
            if (reader != null) {
                try {
                    reader.close();
                } catch (IOException e) {
                    System.out.println("Couldn't close reader: " + e.getMessage());
                    System.exit(0);
                }
            }
        }
    }

    /**
     * Inserts the Data into the table using a batch statement.
     * @param connection
     * @throws SQLException
     */
    private static void insertData(Connection connection) throws SQLException {
        // Creates a prepared statement to insert the data.
        PreparedStatement statement = connection.prepareStatement("INSERT INTO " + "milk_yeild_day0" + " VALUES (?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");
        // Goes through all of the data and inserts it into the prepared statement in a batch.
        for (int x = 0; x < data.size(); x++) {
            String[] elements = data.get(x).split(",");

            int earTag = Integer.parseInt(elements[0]);
            int LACT_NO = Integer.parseInt(elements[1]);
            String MILK_DATE =(elements[2]);
            int Feed_GROUP = Integer.parseInt(elements[3]);
            double Yield1 = Double.parseDouble(elements[4]);
            double PeakFlow = Double.parseDouble(elements[5]);
            String Duration =(elements[6]);
            int StallPostition =Integer.parseInt(elements[7]);
            String RealTime =(elements[8]);
            double Yield2 = Double.parseDouble(elements[9]);
            double PeakFlow2 = Double.parseDouble(elements[10]);
            String Duration2 =(elements[11]);
            int StallPostition2 =Integer.parseInt(elements[12]);
            String RealTime2 =(elements[13]);
            double Yield3 = Double.parseDouble(elements[14]);
            double PeakFlow3 = Double.parseDouble(elements[15]);
            String Duration3 =(elements[16]);
            int StallPostition3 =Integer.parseInt(elements[17]);
            String RealTime3 =(elements[18]);
            double Daily_Yeild = Double.parseDouble(elements[19]);
            String MILK_DATE_MON =(elements[20]);
            String MILK_DATE_TUE =(elements[21]);
            String MILK_DATE_WED =(elements[22]);
            String MILK_DATE_THU =(elements[23]);
            String MILK_DATE_FRI =(elements[24]);

            statement.setInt(1, earTag);
            statement.setInt(2, LACT_NO);
            statement.setString(3, MILK_DATE);
            statement.setInt(4, Feed_GROUP);
            statement.setDouble(5,Yield1);
            statement.setDouble(6,PeakFlow);
            statement.setString(7, Duration);
            statement.setInt(8, StallPostition);
            statement.setString(9, RealTime);
            statement.setDouble(10,Yield2);
            statement.setDouble(11,PeakFlow2);
            statement.setString(12, Duration2);
            statement.setInt(13, StallPostition2);
            statement.setString(14, RealTime2);
            statement.setDouble(15,Yield3);
            statement.setDouble(16,PeakFlow3);
            statement.setString(17, Duration3);
            statement.setInt(18, StallPostition3);
            statement.setString(19, RealTime3);
            statement.setDouble(20,Daily_Yeild);
            statement.setString(21, MILK_DATE_MON);
            statement.setString(22, MILK_DATE_TUE);
            statement.setString(23, MILK_DATE_WED);
            statement.setString(24, MILK_DATE_THU);
            statement.setString(25, MILK_DATE_FRI);



            // A batch is used in order to execute all of the inserts at once.

            statement.addBatch();
        }
        // Inserts all of the data at once, commits the data in order to validate the inputs manually.

        System.out.println("hello");
        statement.executeBatch();
        System.out.println("hello");
        //connection.commit();
        statement.close();
    }


    /**
     * Checks to see if a String variable can be parsed as a double.
     * @param tocheck
     * @return
     */
    private static boolean checkDouble(String tocheck) {
        try {
            Double.parseDouble(tocheck);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    /**
     * Prints resuolts for a query
     * @param resultSet
     * @throws SQLException
     */
    private static void printResults(ResultSet resultSet) throws SQLException {
        // Gets the MetaData in order to print out all of the results.
        ResultSetMetaData data = resultSet.getMetaData();
        // Gets the number of columns produced from the query.
        int columns = data.getColumnCount();
        // Goes through all results.
        while (resultSet.next()) {
            // Goes through all of columns except for the last one in order to format it correctly by using commas.
            for (int i = 1; i < columns; i++) {
                // If a null value is printed, print out null to deal with null pointer exceptions.
                if (resultSet.getString(i) == null) {
                    System.out.print("Null, ");
                } else {
                    // Checks to see if the number can be parsed as a double as there are some double values.
                    if (checkDouble(resultSet.getString(i))) {
                        // Stores the double value and prints it out in the required format.
                        double temp = resultSet.getDouble(i);
                        System.out.print(format.format(temp) + ", ");
                    } else {
                        // Prints out the string if no formatting is required.
                        System.out.print(resultSet.getString(i) + ", ");
                    }
                }
            }
            // Prints out the last column with no comma, using the validation above.
            // If a null value is printed, print out null to deal with null pointer exceptions.
            if (resultSet.getString(columns) == null) {
                System.out.println("Null");
            } else {
                if (checkDouble(resultSet.getString(columns))) {
                    double temp = resultSet.getDouble(columns);
                    System.out.println(format.format(temp));
                } else {
                    System.out.println(resultSet.getString(columns));
                }
            }
        }
    }
}
