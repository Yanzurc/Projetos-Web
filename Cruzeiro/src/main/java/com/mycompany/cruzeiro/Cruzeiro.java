package com.mycompany.cruzeiro;

import Entidades.fila;
import java.util.Locale;
import java.util.Scanner;

public class Cruzeiro {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner sc = new Scanner(System.in);

        fila fila = new fila(10); // Definindo o tamanho máximo das filas

        int opcao = 0;

        while (opcao != 6) {
            System.out.println("\nMenu de opções:");
            System.out.println("1. Solicitar nova senha (Comum ou Prioridade)");
            System.out.println("2. Listar todas as senhas");
            System.out.println("3. Visualizar próximo a ser atendido");
            System.out.println("4. Chamar próximo a ser atendido");
            System.out.println("5. Excluir uma senha");
            System.out.println("6. Sair");
            System.out.print("Escolha uma opção: ");
            
            // Lê a opção e consome a quebra de linha
            opcao = sc.nextInt();
            sc.nextLine();  // Consome a quebra de linha após a entrada do número

            if (opcao == 1) {
                System.out.print("Digite o nome do paciente: ");
                String nome = sc.nextLine();
                
                System.out.print("A senha é prioritária? (s/n): ");
                String prioridadeInput = sc.next().toLowerCase();
                sc.nextLine();  // Consome a quebra de linha após a entrada de 's' ou 'n'
                boolean prioridade = prioridadeInput.equals("s");
                
                fila.solicitarSenha(nome, prioridade);
            } else if (opcao == 2) {
                fila.listarSenhas();
            } else if (opcao == 3) {
                fila.visualizarProximo();
            } else if (opcao == 4) {
                fila.chamarProximo();
            } else if (opcao == 5) {
                System.out.print("Digite o nome do paciente para excluir: ");
                String nome = sc.nextLine();
                fila.excluirSenha(nome);
            } else if (opcao == 6) {
                System.out.println("Saindo...");
            } else {
                System.out.println("Opção inválida. Tente novamente.");
            }
        }

        sc.close();
    }
}
