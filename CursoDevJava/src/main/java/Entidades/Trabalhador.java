/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Entidades;
import Entidades.Enum.Enum;
import java.util.ArrayList;
import java.util.List;
/**
 *
 * @author Yan Cruz
 */
public class Trabalhador {
    private String nome;
    private Enum nivel;
    private double baseSalarial;
    
    private Departamento departamento;
    private List<ContratoHora> contrato = new ArrayList<>();
    
    public Trabalhador(){
    }

    public Trabalhador(String nome, Enum nivel, double baseSalarial, Departamento departamento) {
        this.nome = nome;
        this.nivel = nivel;
        this.baseSalarial = baseSalarial;
        this.departamento = departamento;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Enum getNivel() {
        return nivel;
    }

    public void setNivel(Enum nivel) {
        this.nivel = nivel;
    }

    public double getBaseSalarial() {
        return baseSalarial;
    }

    public void setBaseSalarial(double baseSalarial) {
        this.baseSalarial = baseSalarial;
    }

    public Departamento getDepartamento() {
        return departamento;
    }

    public void setDepartamento(Departamento departamento) {
        this.departamento = departamento;
    }
    
    
}
