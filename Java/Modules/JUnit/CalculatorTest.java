package org.example;

import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.*;
    @TestMethodOrder(MethodOrderer.OrderAnnotation.class)
class CalculatorTest {
    private Calculator calculator;
    @BeforeAll
    static void connectDb(){
        System.out.println("Connected");
    }
    @BeforeEach
    void setup(){
        calculator = new Calculator();
    }
    @Order(2)
    @Test
    void add() {
        int output = calculator.add(10,10);
        int expectedOutput = 20;
        assertEquals(expectedOutput, output);
    }
    @Order(1)
    @Test
    void add1() {
        int output = calculator.add(20,10);
        int expectedOutput = 30;
        assertEquals(expectedOutput, output);
    }

    @AfterEach
    void tearDown(){
        calculator = null;
    }
    @AfterAll
    static void closeDb(){
        System.out.println("Connection closed");
    }
}