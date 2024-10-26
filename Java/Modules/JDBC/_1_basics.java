import java.sql.*;

//postgresql

public class _1_basics {

    private static final String URL = "jdbc:postgresql://localhost:5432/resqit";
    private static final String USER = "burn";
    private static final String PASSWORD = "burn";

    public static void main(String[] args) {
        try {
            Connection connection = getConnection();

            // Example usages
            selectData(connection);
            insertData(connection, "John Doe", "Manager");
            updateData(connection, "Sales");
            batchInsert(connection);

            connection.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    // Establish connection
    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL, USER, PASSWORD);
    }

    // Select data example
    public static void selectData(Connection connection) throws SQLException {
        String selectSQL = "SELECT * FROM userdata";
        Statement statement = connection.createStatement();
        ResultSet resultSet = statement.executeQuery(selectSQL);

        while (resultSet.next()) {
            System.out.println("Name: " + resultSet.getString("name") + ", Position: " + resultSet.getString("position"));
        }
        resultSet.close();
        statement.close();
    }

    // Insert data example
    public static void insertData(Connection connection, String name, String position) throws SQLException {
        String insertSQL = "INSERT INTO userdata (name, position) VALUES (?, ?)";
        PreparedStatement preparedStatement = connection.prepareStatement(insertSQL);
        preparedStatement.setString(1, name);
        preparedStatement.setString(2, position);
        int rowsAffected = preparedStatement.executeUpdate();
        System.out.println("Rows inserted: " + rowsAffected);
        preparedStatement.close();
    }

    // Update data with transaction management
    public static void updateData(Connection connection, String department) throws SQLException {
        connection.setAutoCommit(false);
        String updateSQL = "UPDATE userdata SET salary = salary * 1.1 WHERE department = ?";
        try (PreparedStatement preparedStatement = connection.prepareStatement(updateSQL)) {
            preparedStatement.setString(1, department);
            int rowsAffected = preparedStatement.executeUpdate();
            System.out.println("Rows updated: " + rowsAffected);
            connection.commit();
        } catch (SQLException e) {
            connection.rollback();
            e.printStackTrace();
        }
    }

    // Batch insert example
    public static void batchInsert(Connection connection) throws SQLException {
        Statement batchStatement = connection.createStatement();
        batchStatement.addBatch("INSERT INTO userdata (name) VALUES ('Alice')");
        batchStatement.addBatch("INSERT INTO userdata (name) VALUES ('Bob')");
        int[] batchResults = batchStatement.executeBatch();
        System.out.println("Batch insert completed. Rows affected: " + batchResults.length);
        batchStatement.close();
    }
}


// Explicit loading (optional)
// Class.forName("org.postgresql.Driver");

/*
 * <dependency>
    <groupId>org.postgresql</groupId>
    <artifactId>postgresql</artifactId>
    <version>42.2.5</version>
    </dependency>
 */