-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema hotel
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema hotel
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `hotel` ;
USE `hotel` ;

-- -----------------------------------------------------
-- Table `hotel`.`hospede`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel`.`hospede` (
  `idhospede` INT primary key  NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NULL,
  `cpf` VARCHAR(15) NULL,
  `rg` VARCHAR(45) NULL,
  `telefone` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `senha` VARCHAR(255) NULL);
  


-- -----------------------------------------------------
-- Table `hotel`.`servicos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel`.`servicos` (
  `idservicos` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `custo` VARCHAR(45) NULL,
  PRIMARY KEY (`idservicos`))
ENGINE = InnoDB;
show tables;

-- -----------------------------------------------------
-- Table `hotel`.`administrador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel`.`administrador` (
  `idadm` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(255) NULL,
  `cpf` VARCHAR(15) NULL,
  `rg` VARCHAR(45) NULL,
  `telefone` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `senha` VARCHAR(255) NULL,
  PRIMARY KEY (`idadm`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotel`.`quarto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel`.`quarto` (
  `idquarto` INT NOT NULL AUTO_INCREMENT,
  `numero` INT NULL,
  `tipo` VARCHAR(45) NULL,
  `custo_quarto` VARCHAR(9) NULL,
  `status` INT NULL,
  `administrador_idadm` INT NOT NULL,
  PRIMARY KEY (`idquarto`, `administrador_idadm`),
  `fk_quarto_administrador1_idx` int,
  CONSTRAINT `fk_quarto_administrador1`
    FOREIGN KEY (`administrador_idadm`)
    REFERENCES `hotel`.`administrador` (`idadm`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `hotel`.`solicita`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel`.`solicita` (
  idsolicita int primary key auto_increment,
  `fk_idservicos` INT NOT NULL,
  `fk_idhospede` INT NOT NULL);
  alter table solicita add
  CONSTRAINT `fk_hospede_id`
    FOREIGN KEY (`fk_idhospede`)
    REFERENCES `hotel`.`hospede` (`idshospede`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION;
    alter table solicita add
  CONSTRAINT `fk_hospede_id`
    FOREIGN KEY (`fk_idhospede`)
    REFERENCES `hotel`.`hospede` (`idhospede`);


-- alter table reserva drop constraint fk_cliente_has_quarto_quarto1
-- -----------------------------------------------------
-- Table `hotel`.`reserva`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `hotel`.`reserva` (
  `idreserva` INT primary key AUTO_INCREMENT,
  `hospede_idhospede` INT NULL,
  `data_reserva` DATE NULL,
  `data_entrada` DATE NULL,
  `data_saida` DATE NULL,
  `valor_total` VARCHAR(45) NULL,
  fk_idquarto int,
  `status` VARCHAR(45) NULL,
  CONSTRAINT `fk_cliente_has_quarto_cliente1`
    FOREIGN KEY (`hospede_idhospede`)
    REFERENCES `hotel`.`hospede` (`idhospede`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_hospede_has_quarto_quarto1`
    FOREIGN KEY (`fk_idquarto`)
    REFERENCES `hotel`.`quarto` (`idquarto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_reserva_administrador1`
    FOREIGN KEY (`administrador_idadm`)
    REFERENCES `hotel`.`administrador` (`idadm`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
drop table baixa;
create table baixa(
idbaixa int primary key auto_increment, 
fk_idreserva_b int,
fk_administrador int,
constraint fk_baixa_reserva_b foreign key(fk_idreserva_b) references reserva(idreserva),
constraint fk_baixa_adm foreign key(fk_administrador) references administrador(idadm)
);
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;