package Entidades;

public class fila {
    private String[] filaComum;
    private String[] filaPrioridade;
    private int tamanhoComum;
    private int tamanhoPrioridade;
    private int contadorAtendimentos;
    private int maxSize;

    public fila(int maxSize) {
        this.maxSize = maxSize;
        filaComum = new String[maxSize];
        filaPrioridade = new String[maxSize];
        tamanhoComum = 0;
        tamanhoPrioridade = 0;
        contadorAtendimentos = 0;
    }

    
    public void solicitarSenha(String nome, boolean prioridade) {
        if (prioridade) {
            if (tamanhoPrioridade < maxSize) {
                filaPrioridade[tamanhoPrioridade++] = nome;
                System.out.println("Senha prioridade solicitada para: " + nome);
            } else {
                System.out.println("Fila de prioridade cheia!");
            }
        } else {
            if (tamanhoComum < maxSize) {
                filaComum[tamanhoComum++] = nome;
                System.out.println("Senha comum solicitada para: " + nome);
            } else {
                System.out.println("Fila comum cheia!");
            }
        }
    }

    
    public void listarSenhas() {
        System.out.println("Senhas comuns:");
        for (int i = 0; i < tamanhoComum; i++) {
            System.out.print(filaComum[i] + " ");
        }
        System.out.println("\nSenhas prioritárias:");
        for (int i = 0; i < tamanhoPrioridade; i++) {
            System.out.print(filaPrioridade[i] + " ");
        }
        System.out.println();
    }

    
    public void visualizarProximo() {
        if (tamanhoPrioridade > 0) {
            System.out.println("Próxima senha prioritária: " + filaPrioridade[0]);
        } else if (tamanhoComum > 0) {
            System.out.println("Próxima senha comum: " + filaComum[0]);
        } else {
            System.out.println("Nenhuma senha na fila.");
        }
    }

    
    public void chamarProximo() {
        if (contadorAtendimentos < 2 && tamanhoPrioridade > 0) {
            System.out.println("Chamando senha prioritária: " + filaPrioridade[0]);
            removerFila(filaPrioridade, tamanhoPrioridade--);
            contadorAtendimentos++;
        } else if (tamanhoComum > 0) {
            System.out.println("Chamando senha comum: " + filaComum[0]);
            removerFila(filaComum, tamanhoComum--);
            contadorAtendimentos = 0; // reseta o contador após chamar um comum
        } else if (tamanhoPrioridade > 0) {
            System.out.println("Chamando senha prioritária: " + filaPrioridade[0]);
            removerFila(filaPrioridade, tamanhoPrioridade--);
        } else {
            System.out.println("Nenhuma senha disponível para chamar.");
        }
    }

    
    private void removerFila(String[] fila, int tamanho) {
        for (int i = 0; i < tamanho - 1; i++) {
            fila[i] = fila[i + 1];
        }
        fila[tamanho - 1] = null; 
    }

    
    public void excluirSenha(String nome) {
        boolean encontrado = false;

        
        for (int i = 0; i < tamanhoPrioridade; i++) {
            if (filaPrioridade[i].equals(nome)) {
                removerFila(filaPrioridade, tamanhoPrioridade--);
                System.out.println("Senha prioritária de " + nome + " excluída.");
                encontrado = true;
                break;
            }
        }

        
        if (!encontrado) {
            for (int i = 0; i < tamanhoComum; i++) {
                if (filaComum[i].equals(nome)) {
                    removerFila(filaComum, tamanhoComum--);
                    System.out.println("Senha comum de " + nome + " excluída.");
                    encontrado = true;
                    break;
                }
            }
        }

        if (!encontrado) {
            System.out.println("Senha não encontrada.");
        }
    }
}
