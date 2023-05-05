package exercicio01;

public class TesteCalculadora {
        public static void main(String[] args) {

            CalculadoraCientifica calculadora_cientifica = new CalculadoraCientifica();
            CalculadoraFinanceira calculadora_financeira = new CalculadoraFinanceira();
            CalculadoraProgramadora calculadora_programadora = new CalculadoraProgramadora();

            double resultadoLog = calculadora_cientifica.calcularLogaritmo(10, 2);
            System.out.println("Logaritmo de 10 na base 2: " + resultadoLog);

            double jurosSimples = calculadora_financeira.calcularJuros(1000, 0.1, 5);
            System.out.println("Juros simples de R$1000 a uma taxa de 10% ao ano em 5 anos: R$" + jurosSimples);

            double jurosCompostos = calculadora_financeira.calcularJurosCompostos(1000, 0.1, 5);
            System.out.println("Juros compostos de R$1000 a uma taxa de 10% ao ano em 5 anos: R$" + jurosCompostos);

            int resultadoAnd = calculadora_programadora.calcularBitwiseAnd(12, 25);
            System.out.println("AND bitwise de 12 e 25: " + resultadoAnd);

            int resultadoOr = calculadora_programadora.calcularBitwiseOr(12, 25);
            System.out.println("OR bitwise de 12 e 25: " + resultadoOr);

            int resultadoXor = calculadora_programadora.calcularBitwiseXor(12, 25);
            System.out.println("XOR bitwise de 12 e 25: " + resultadoXor);
        }
    }

