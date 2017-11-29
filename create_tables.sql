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
-- Table `shopping_mall`.`User`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shopping_mall`.`회원` (
  `이메일` CHAR(30) NOT NULL,
  `이름` VARCHAR(45) NOT NULL,
  `암호` VARCHAR(45) NOT NULL,
  `주소` VARCHAR(100) NULL,
  `전화번호` VARCHAR(45) NULL,
  `레벨` TINYINT(1) NOT NULL,
  PRIMARY KEY (`이메일`)
)ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `shopping_mall`.`Goods`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shopping_mall`.`상품` (
  `상품아이디` INT NOT NULL AUTO_INCREMENT,
  `판매자` CHAR(30) NOT NULL,
  `상품정보` TEXT NULL,
  PRIMARY KEY (`상품아이디`),
  constraint `fk_1` foreign key (`판매자`) references `회원` (`이메일`)
) ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `shopping_mall`.`Order`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shopping_mall`.`주문` (
  `상품아이디` INT NOT NULL,
  `주문자` CHAR(30) NOT NULL,
  `주문일시` DATETIME(5),
  `수량` INT NOT NULL,
  `메모` varchar(100) NULL,
constraint `fk_2` FOREIGN KEY (상품아이디) REFERENCES 상품 (상품아이디),
constraint `fk_3` foreign key (주문자) references 회원 (이메일)
) ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
