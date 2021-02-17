
-- -----------------------------------------------------
-- Creation de la base de données agregateur_db
-- -----------------------------------------------------

CREATE DATABASE agregateur_db CHARACTER SET 'utf8';
USE agregateur_db;
-- -----------------------------------------------------
-- Table `utilisateur`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `utilisateur_id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL,
  `surnom` VARCHAR(80) NOT NULL,
  `ville` VARCHAR(80) NULL,
  `pays` VARCHAR(80) NULL,
  `avatar` VARCHAR(255) NULL,
  `biographie` LONGTEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `mot_de_passe` VARCHAR(255) NULL,
  PRIMARY KEY (`utilisateur_id`),
  UNIQUE INDEX `email_UNIQUE` (`email`) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `flux_information`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `flux_information` (
  `flux_id` INT NOT NULL AUTO_INCREMENT,
  `titre` VARCHAR(100) NOT NULL,
  `description` LONGTEXT NULL,
  `adresse_site_web` VARCHAR(255) NOT NULL,
  `url_publications` VARCHAR(255) NOT NULL,
  `langue` VARCHAR(8) NULL,
  PRIMARY KEY (`flux_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `publication`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `publication` (
  `publication_id` INT NOT NULL AUTO_INCREMENT,
  `titre` VARCHAR(100) NOT NULL,
  `lien_publication` VARCHAR(255) ,
  `date_timestamp` DATETIME ,
  `date_publication` DATETIME NULL,
  `description` LONGTEXT NULL,
  `flux_id` INT NULL,
  PRIMARY KEY (`publication_id`),
  INDEX `fk_publication_flux_information1_idx` (`flux_id` ASC) VISIBLE,
  CONSTRAINT `fk_publication_flux_information1`
    FOREIGN KEY (`flux_id`)
    REFERENCES `flux_information` (`flux_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `lecture_publication`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `lecture_publication` (
  `lecture_id` INT NOT NULL AUTO_INCREMENT,
  `date_lecture` DATETIME NULL,
  `utilisateur_id` INT NULL,
  `publication_id` INT NULL,
  PRIMARY KEY (`lecture_id`),
  UNIQUE INDEX `lecture_id_UNIQUE` (`lecture_id` ASC) VISIBLE,
  INDEX `fk_lecture_publication_utilisateur1_idx` (`utilisateur_id` ASC) VISIBLE,
  INDEX `fk_lecture_publication_publication1_idx` (`publication_id` ASC) VISIBLE,
  CONSTRAINT `fk_lecture_publication_utilisateur1`
    FOREIGN KEY (`utilisateur_id`)
    REFERENCES `utilisateur` (`utilisateur_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `fk_lecture_publication_publication1`
    FOREIGN KEY (`publication_id`)
    REFERENCES `publication` (`publication_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `partage_id`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `partage` (
  `partage_id` INT NOT NULL AUTO_INCREMENT,
  `date_partage` DATETIME ,
  `commentaire` LONGTEXT NULL,
  `utilisateur_id` INT NULL,
  `publication_id` INT NULL,
  PRIMARY KEY (`partage_id`),
  UNIQUE INDEX `lecture_id_UNIQUE` (`partage_id` ASC) VISIBLE,
  INDEX `fk_partage_id_utilisateur1_idx` (`utilisateur_id` ASC) VISIBLE,
  INDEX `fk_partage_id_publication1_idx` (`publication_id` ASC) VISIBLE,
  CONSTRAINT `fk_partage_id_utilisateur1`
    FOREIGN KEY (`utilisateur_id`)
    REFERENCES `utilisateur` (`utilisateur_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE,
  CONSTRAINT `fk_partage_id_publication1`
    FOREIGN KEY (`publication_id`)
    REFERENCES `publication` (`publication_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `commentaire`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `commentaire` (
  `commentaire_id` INT NOT NULL AUTO_INCREMENT,
  `date_commentaire` DATETIME NULL,
  `commentaire` LONGTEXT NULL,
  `utilisateur_id` INT NOT NULL,
  `publication_id` INT NULL,
  PRIMARY KEY (`commentaire_id`),
  UNIQUE INDEX `lecture_id_UNIQUE` (`commentaire_id` ASC) VISIBLE,
  INDEX `fk_commentaire_utilisateur1_idx` (`utilisateur_id` ASC) VISIBLE,
  INDEX `fk_commentaire_publication1_idx` (`publication_id` ASC) VISIBLE,
  CONSTRAINT `fk_commentaire_utilisateur1`
    FOREIGN KEY (`utilisateur_id`)
    REFERENCES `utilisateur` (`utilisateur_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_commentaire_publication1`
    FOREIGN KEY (`publication_id`)
    REFERENCES `publication` (`publication_id`)
    ON DELETE SET NULL
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `souscription`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `souscription` (
  `souscription_id` INT NOT NULL AUTO_INCREMENT,
  `date_souscription` DATETIME NULL,
  `utilisateur_id` INT NOT NULL,
  `flux_id` INT NOT NULL,
  PRIMARY KEY (`souscription_id`),
  UNIQUE INDEX `lecture_id_UNIQUE` (`souscription_id` ASC) VISIBLE,
  INDEX `fk_souscription_utilisateur1_idx` (`utilisateur_id` ASC) VISIBLE,
  INDEX `fk_souscription_flux_information1_idx` (`flux_id` ASC) VISIBLE,
  CONSTRAINT `fk_souscription_utilisateur1`
    FOREIGN KEY (`utilisateur_id`)
    REFERENCES `utilisateur` (`utilisateur_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_souscription_flux_information1`
    FOREIGN KEY (`flux_id`)
    REFERENCES `flux_information` (`flux_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `amitie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `amitie` (
  `amitie_id` INT NOT NULL AUTO_INCREMENT,
  `date_demande` DATETIME NULL,
  `statut` TINYINT(1) NULL,
  `destinataire_id` INT NULL,
  `utilisateur_id` INT NOT NULL,
  PRIMARY KEY (`amitie_id`),
  UNIQUE INDEX `amitie_id_UNIQUE` (`amitie_id` ASC) VISIBLE,
  INDEX `fk_amitie_utilisateur1_idx` (`utilisateur_id` ASC) VISIBLE,
  CONSTRAINT `fk_amitie_utilisateur1`
    FOREIGN KEY (`utilisateur_id`)
    REFERENCES `utilisateur` (`utilisateur_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


