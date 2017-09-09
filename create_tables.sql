-- MySQL Script generated by MySQL Workbench
-- 2017년 09월 09일 (토) 오후 05시 32분 16초
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema shopping_mall
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema shopping_mall
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `shopping_mall` DEFAULT CHARACTER SET utf8 ;
USE `shopping_mall` ;

-- -----------------------------------------------------
-- Table `shopping_mall`.`Goods`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shopping_mall`.`Goods` (
  `상품아이디` INT NOT NULL AUTO_INCREMENT,
  `판매자` CHAR(30) NOT NULL,
  `상품정보` TEXT NULL,
  PRIMARY KEY (`상품아이디`))
ENGINE = InnoDB
COMMENT = '상품정보';


-- -----------------------------------------------------
-- Table `shopping_mall`.`Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shopping_mall`.`Order` (
  `상품아이디` INT NOT NULL,
  `주문자` CHAR(30) NULL,
  `주문일시` DATETIME(20) NOT NULL,
  PRIMARY KEY (`상품아이디`),
  CONSTRAINT `상품아이디`
    FOREIGN KEY (`상품아이디`)
    REFERENCES `shopping_mall`.`Goods` (`상품아이디`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `shopping_mall`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shopping_mall`.`User` (
  `이메일` CHAR(30) NOT NULL,
  `이름` VARCHAR(45) NOT NULL,
  `암호` VARCHAR(45) NOT NULL,
  `주소` VARCHAR(100) NULL,
  `전화번호` VARCHAR(45) NULL,
  `레벨` TINYINT(1) NOT NULL,
  PRIMARY KEY (`이메일`),
  CONSTRAINT `주문자`
    FOREIGN KEY ()
    REFERENCES `shopping_mall`.`Order` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `판매자`
    FOREIGN KEY ()
    REFERENCES `shopping_mall`.`Order` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
