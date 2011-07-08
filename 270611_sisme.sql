-- MySQL dump 10.13  Distrib 5.1.47, for unknown-linux-gnu (x86_64)
--
-- Host: localhost    Database: simasnio_sisme
-- ------------------------------------------------------
-- Server version	5.1.56-community-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Contraparte'),(2,'Equipo Fed');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM AUTO_INCREMENT=100 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
INSERT INTO `auth_group_permissions` VALUES (1,1,58),(2,1,59),(3,1,60),(99,2,66),(98,2,65),(97,2,64),(96,2,63),(95,2,62),(94,2,61),(93,2,60),(92,2,59),(91,2,58),(90,2,57),(89,2,56),(88,2,55),(87,2,54),(86,2,53),(85,2,52),(84,2,51),(83,2,50),(82,2,49),(81,2,48),(80,2,47),(79,2,46),(78,2,39),(77,2,38),(76,2,37),(75,2,36),(74,2,35),(73,2,34);
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_message`
--

DROP TABLE IF EXISTS `auth_message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_message` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `auth_message_fbfc09f1` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_message`
--

LOCK TABLES `auth_message` WRITE;
/*!40000 ALTER TABLE `auth_message` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=127 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add user',3,'add_user'),(8,'Can change user',3,'change_user'),(9,'Can delete user',3,'delete_user'),(10,'Can add message',4,'add_message'),(11,'Can change message',4,'change_message'),(12,'Can delete message',4,'delete_message'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(25,'Can add migration history',9,'add_migrationhistory'),(26,'Can change migration history',9,'change_migrationhistory'),(27,'Can delete migration history',9,'delete_migrationhistory'),(28,'Can add departamento',10,'add_departamento'),(29,'Can change departamento',10,'change_departamento'),(30,'Can delete departamento',10,'delete_departamento'),(31,'Can add municipio',11,'add_municipio'),(32,'Can change municipio',11,'change_municipio'),(33,'Can delete municipio',11,'delete_municipio'),(34,'Can add Organización',12,'add_organizacion'),(35,'Can change Organización',12,'change_organizacion'),(36,'Can delete Organización',12,'delete_organizacion'),(37,'Can add donante',13,'add_donante'),(38,'Can change donante',13,'change_donante'),(39,'Can delete donante',13,'delete_donante'),(40,'Can add Tema de FED',14,'add_tema'),(41,'Can change Tema de FED',14,'change_tema'),(42,'Can delete Tema de FED',14,'delete_tema'),(43,'Can add resultado',15,'add_resultado'),(44,'Can change resultado',15,'change_resultado'),(45,'Can delete resultado',15,'delete_resultado'),(46,'Can add proyecto',16,'add_proyecto'),(47,'Can change proyecto',16,'change_proyecto'),(48,'Can delete proyecto',16,'delete_proyecto'),(49,'Can add Tema de trabajo',17,'add_tematrabajo'),(50,'Can change Tema de trabajo',17,'change_tematrabajo'),(51,'Can delete Tema de trabajo',17,'delete_tematrabajo'),(52,'Can add Población Meta Directa',18,'add_poblacionmetadirecta'),(53,'Can change Población Meta Directa',18,'change_poblacionmetadirecta'),(54,'Can delete Población Meta Directa',18,'delete_poblacionmetadirecta'),(55,'Can add Población Meta Indirecta',19,'add_poblacionmetaindirecta'),(56,'Can change Población Meta Indirecta',19,'change_poblacionmetaindirecta'),(57,'Can delete Población Meta Indirecta',19,'delete_poblacionmetaindirecta'),(58,'Can add informe',20,'add_informe'),(59,'Can change informe',20,'change_informe'),(60,'Can delete informe',20,'delete_informe'),(61,'Can add accion impulsada',21,'add_accionimpulsada'),(62,'Can change accion impulsada',21,'change_accionimpulsada'),(63,'Can delete accion impulsada',21,'delete_accionimpulsada'),(64,'Can add accion implementada',22,'add_accionimplementada'),(65,'Can change accion implementada',22,'change_accionimplementada'),(66,'Can delete accion implementada',22,'delete_accionimplementada'),(67,'Can add Comisión',23,'add_comision'),(68,'Can change Comisión',23,'change_comision'),(69,'Can delete Comisión',23,'delete_comision'),(70,'Can add participacion comision',24,'add_participacioncomision'),(71,'Can change participacion comision',24,'change_participacioncomision'),(72,'Can delete participacion comision',24,'delete_participacioncomision'),(73,'Can add Acción de agenda',25,'add_accionagenda'),(74,'Can change Acción de agenda',25,'change_accionagenda'),(75,'Can delete Acción de agenda',25,'delete_accionagenda'),(76,'Can add agenda publica',26,'add_agendapublica'),(77,'Can change agenda publica',26,'change_agendapublica'),(78,'Can delete agenda publica',26,'delete_agendapublica'),(79,'Can add Tipo de Observatorio',27,'add_tipoobservatorio'),(80,'Can change Tipo de Observatorio',27,'change_tipoobservatorio'),(81,'Can delete Tipo de Observatorio',27,'delete_tipoobservatorio'),(82,'Can add observatorio',28,'add_observatorio'),(83,'Can change observatorio',28,'change_observatorio'),(84,'Can delete observatorio',28,'delete_observatorio'),(85,'Can add Acción de demanda',29,'add_acciondemanda'),(86,'Can change Acción de demanda',29,'change_acciondemanda'),(87,'Can delete Acción de demanda',29,'delete_acciondemanda'),(88,'Can add Demanda de Justicia',30,'add_demandajusticia'),(89,'Can change Demanda de Justicia',30,'change_demandajusticia'),(90,'Can delete Demanda de Justicia',30,'delete_demandajusticia'),(91,'Can add Denuncia',31,'add_denuncia'),(92,'Can change Denuncia',31,'change_denuncia'),(93,'Can delete Denuncia',31,'delete_denuncia'),(94,'Can add Posee información',32,'add_poseeninfo'),(95,'Can change Posee información',32,'change_poseeninfo'),(96,'Can delete Posee información',32,'delete_poseeninfo'),(97,'Can add Recibe información',33,'add_recibeninfo'),(98,'Can change Recibe información',33,'change_recibeninfo'),(99,'Can delete Recibe información',33,'delete_recibeninfo'),(100,'Can add Prevención de VBG',34,'add_prevencionvbg'),(101,'Can change Prevención de VBG',34,'change_prevencionvbg'),(102,'Can delete Prevención de VBG',34,'delete_prevencionvbg'),(103,'Can add Masculinidad Libre',35,'add_masculinidadlibre'),(104,'Can change Masculinidad Libre',35,'change_masculinidadlibre'),(105,'Can delete Masculinidad Libre',35,'delete_masculinidadlibre'),(106,'Can add caso atendido',36,'add_casoatendido'),(107,'Can change caso atendido',36,'change_casoatendido'),(108,'Can delete caso atendido',36,'delete_casoatendido'),(109,'Can add denuncia interpuesta',37,'add_denunciainterpuesta'),(110,'Can change denuncia interpuesta',37,'change_denunciainterpuesta'),(111,'Can delete denuncia interpuesta',37,'delete_denunciainterpuesta'),(112,'Can add Atención a Mujeres',38,'add_atencionmujer'),(113,'Can change Atención a Mujeres',38,'change_atencionmujer'),(114,'Can delete Atención a Mujeres',38,'delete_atencionmujer'),(115,'Can add Referencia y Contrareferencia',39,'add_referenciacontrareferencia'),(116,'Can change Referencia y Contrareferencia',39,'change_referenciacontrareferencia'),(117,'Can delete Referencia y Contrareferencia',39,'delete_referenciacontrareferencia'),(118,'Can add Capacidad Administrativa',40,'add_capacidadadmitiva'),(119,'Can change Capacidad Administrativa',40,'change_capacidadadmitiva'),(120,'Can delete Capacidad Administrativa',40,'delete_capacidadadmitiva'),(121,'Can add Medir y Reportar',41,'add_medirreportar'),(122,'Can change Medir y Reportar',41,'change_medirreportar'),(123,'Can delete Medir y Reportar',41,'delete_medirreportar'),(124,'Can add Plan Estratégico',42,'add_planestrategico'),(125,'Can change Plan Estratégico',42,'change_planestrategico'),(126,'Can delete Plan Estratégico',42,'delete_planestrategico');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'admin','','','hemygb@gmail.com','sha1$c83ba$13d908d3ddfc712010cc1a1e66d0f86646a552af',1,1,1,'2011-06-21 16:49:18','2011-06-09 17:30:29'),(2,'equipofed','','','','sha1$b5a47$c1b4cc977da0fba6856485de6f196f0d899da541',1,1,0,'2011-06-21 11:04:54','2011-06-09 17:42:24');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (1,2,2);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_accionagenda`
--

DROP TABLE IF EXISTS `contraparte_accionagenda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_accionagenda` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_accionagenda`
--

LOCK TABLES `contraparte_accionagenda` WRITE;
/*!40000 ALTER TABLE `contraparte_accionagenda` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_accionagenda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_acciondemanda`
--

DROP TABLE IF EXISTS `contraparte_acciondemanda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_acciondemanda` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_acciondemanda`
--

LOCK TABLES `contraparte_acciondemanda` WRITE;
/*!40000 ALTER TABLE `contraparte_acciondemanda` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_acciondemanda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_accionimplementada`
--

DROP TABLE IF EXISTS `contraparte_accionimplementada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_accionimplementada` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `accion` int(11) NOT NULL,
  `tema_id` int(11) NOT NULL,
  `estado` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_accionimplementada_24ec5559` (`informe_id`),
  KEY `contraparte_accionimplementada_e189947` (`tema_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_accionimplementada`
--

LOCK TABLES `contraparte_accionimplementada` WRITE;
/*!40000 ALTER TABLE `contraparte_accionimplementada` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_accionimplementada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_accionimpulsada`
--

DROP TABLE IF EXISTS `contraparte_accionimpulsada`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_accionimpulsada` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `tipo_accion` int(11) NOT NULL,
  `tema_id` int(11) NOT NULL,
  `hombres` int(11) NOT NULL,
  `mujeres` int(11) NOT NULL,
  `ambito` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_accionimpulsada_24ec5559` (`informe_id`),
  KEY `contraparte_accionimpulsada_e189947` (`tema_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_accionimpulsada`
--

LOCK TABLES `contraparte_accionimpulsada` WRITE;
/*!40000 ALTER TABLE `contraparte_accionimpulsada` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_accionimpulsada` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_agendapublica`
--

DROP TABLE IF EXISTS `contraparte_agendapublica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_agendapublica` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `tipo_accion_id` int(11) NOT NULL,
  `tema_id` int(11) NOT NULL,
  `ambito` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_agendapublica_24ec5559` (`informe_id`),
  KEY `contraparte_agendapublica_64b8c7a5` (`tipo_accion_id`),
  KEY `contraparte_agendapublica_e189947` (`tema_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_agendapublica`
--

LOCK TABLES `contraparte_agendapublica` WRITE;
/*!40000 ALTER TABLE `contraparte_agendapublica` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_agendapublica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_atencionmujer`
--

DROP TABLE IF EXISTS `contraparte_atencionmujer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_atencionmujer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `organizacion` int(11) NOT NULL,
  `tipo_poblacion` int(11) NOT NULL,
  `plan_vida` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_atencionmujer_24ec5559` (`informe_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_atencionmujer`
--

LOCK TABLES `contraparte_atencionmujer` WRITE;
/*!40000 ALTER TABLE `contraparte_atencionmujer` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_atencionmujer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_capacidadadmitiva`
--

DROP TABLE IF EXISTS `contraparte_capacidadadmitiva`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_capacidadadmitiva` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `ha_mejorado` int(11) NOT NULL,
  `atraves` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_capacidadadmitiva_24ec5559` (`informe_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_capacidadadmitiva`
--

LOCK TABLES `contraparte_capacidadadmitiva` WRITE;
/*!40000 ALTER TABLE `contraparte_capacidadadmitiva` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_capacidadadmitiva` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_casoatendido`
--

DROP TABLE IF EXISTS `contraparte_casoatendido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_casoatendido` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `tipo_caso` int(11) NOT NULL,
  `situacion_caso` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_casoatendido_24ec5559` (`informe_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_casoatendido`
--

LOCK TABLES `contraparte_casoatendido` WRITE;
/*!40000 ALTER TABLE `contraparte_casoatendido` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_casoatendido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_comision`
--

DROP TABLE IF EXISTS `contraparte_comision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_comision` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_comision`
--

LOCK TABLES `contraparte_comision` WRITE;
/*!40000 ALTER TABLE `contraparte_comision` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_comision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_demandajusticia`
--

DROP TABLE IF EXISTS `contraparte_demandajusticia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_demandajusticia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `tipo_accion_id` int(11) NOT NULL,
  `poblacion_discriminada` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_demandajusticia_24ec5559` (`informe_id`),
  KEY `contraparte_demandajusticia_64b8c7a5` (`tipo_accion_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_demandajusticia`
--

LOCK TABLES `contraparte_demandajusticia` WRITE;
/*!40000 ALTER TABLE `contraparte_demandajusticia` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_demandajusticia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_denuncia`
--

DROP TABLE IF EXISTS `contraparte_denuncia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_denuncia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `situacion` int(11) NOT NULL,
  `tipo_poblacion` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_denuncia_24ec5559` (`informe_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_denuncia`
--

LOCK TABLES `contraparte_denuncia` WRITE;
/*!40000 ALTER TABLE `contraparte_denuncia` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_denuncia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_denunciainterpuesta`
--

DROP TABLE IF EXISTS `contraparte_denunciainterpuesta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_denunciainterpuesta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `tipo_denuncia` int(11) NOT NULL,
  `instancia_administra` int(11) NOT NULL,
  `situacion_denuncia` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_denunciainterpuesta_24ec5559` (`informe_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_denunciainterpuesta`
--

LOCK TABLES `contraparte_denunciainterpuesta` WRITE;
/*!40000 ALTER TABLE `contraparte_denunciainterpuesta` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_denunciainterpuesta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_informe`
--

DROP TABLE IF EXISTS `contraparte_informe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_informe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `organizacion_id` int(11) NOT NULL,
  `proyecto_id` int(11) NOT NULL,
  `anio_desde` int(11) NOT NULL,
  `mes_desde` int(11) NOT NULL,
  `anio_hasta` int(11) NOT NULL,
  `mes_hasta` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_informe_48753264` (`organizacion_id`),
  KEY `contraparte_informe_cf4ad9cb` (`proyecto_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_informe`
--

LOCK TABLES `contraparte_informe` WRITE;
/*!40000 ALTER TABLE `contraparte_informe` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_informe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_masculinidadlibre`
--

DROP TABLE IF EXISTS `contraparte_masculinidadlibre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_masculinidadlibre` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `tipo_accion` int(11) NOT NULL,
  `tipo_poblacion` int(11) NOT NULL,
  `segmento_poblacional` int(11) NOT NULL,
  `hombres` int(11) NOT NULL,
  `mujeres` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_masculinidadlibre_24ec5559` (`informe_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_masculinidadlibre`
--

LOCK TABLES `contraparte_masculinidadlibre` WRITE;
/*!40000 ALTER TABLE `contraparte_masculinidadlibre` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_masculinidadlibre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_medirreportar`
--

DROP TABLE IF EXISTS `contraparte_medirreportar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_medirreportar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `ha_mejorado` int(11) NOT NULL,
  `manera` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_medirreportar_24ec5559` (`informe_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_medirreportar`
--

LOCK TABLES `contraparte_medirreportar` WRITE;
/*!40000 ALTER TABLE `contraparte_medirreportar` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_medirreportar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_observatorio`
--

DROP TABLE IF EXISTS `contraparte_observatorio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_observatorio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `tipo_observatorio_id` int(11) NOT NULL,
  `accion` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_observatorio_24ec5559` (`informe_id`),
  KEY `contraparte_observatorio_6a016bcb` (`tipo_observatorio_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_observatorio`
--

LOCK TABLES `contraparte_observatorio` WRITE;
/*!40000 ALTER TABLE `contraparte_observatorio` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_observatorio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_participacioncomision`
--

DROP TABLE IF EXISTS `contraparte_participacioncomision`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_participacioncomision` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `tipo_comision_id` int(11) NOT NULL,
  `estado` int(11) NOT NULL,
  `ambito` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_participacioncomision_24ec5559` (`informe_id`),
  KEY `contraparte_participacioncomision_8bc11549` (`tipo_comision_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_participacioncomision`
--

LOCK TABLES `contraparte_participacioncomision` WRITE;
/*!40000 ALTER TABLE `contraparte_participacioncomision` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_participacioncomision` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_planestrategico`
--

DROP TABLE IF EXISTS `contraparte_planestrategico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_planestrategico` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `utiliza_plan` int(11) NOT NULL,
  `manera` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_planestrategico_24ec5559` (`informe_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_planestrategico`
--

LOCK TABLES `contraparte_planestrategico` WRITE;
/*!40000 ALTER TABLE `contraparte_planestrategico` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_planestrategico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_poseeninfo`
--

DROP TABLE IF EXISTS `contraparte_poseeninfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_poseeninfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `tipo_accion` int(11) NOT NULL,
  `tema_id` int(11) NOT NULL,
  `tipo_poblacion` int(11) NOT NULL,
  `segmento_poblacional` int(11) NOT NULL,
  `hombres` int(11) NOT NULL,
  `mujeres` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_poseeninfo_24ec5559` (`informe_id`),
  KEY `contraparte_poseeninfo_e189947` (`tema_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_poseeninfo`
--

LOCK TABLES `contraparte_poseeninfo` WRITE;
/*!40000 ALTER TABLE `contraparte_poseeninfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_poseeninfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_prevencionvbg`
--

DROP TABLE IF EXISTS `contraparte_prevencionvbg`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_prevencionvbg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `tipo_accion` int(11) NOT NULL,
  `tipo_poblacion` int(11) NOT NULL,
  `segmento_poblacional` int(11) NOT NULL,
  `hombres` int(11) NOT NULL,
  `mujeres` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_prevencionvbg_24ec5559` (`informe_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_prevencionvbg`
--

LOCK TABLES `contraparte_prevencionvbg` WRITE;
/*!40000 ALTER TABLE `contraparte_prevencionvbg` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_prevencionvbg` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_recibeninfo`
--

DROP TABLE IF EXISTS `contraparte_recibeninfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_recibeninfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `tipo_accion` int(11) NOT NULL,
  `tipo_poblacion` int(11) NOT NULL,
  `segmento_poblacional` int(11) NOT NULL,
  `hombres` int(11) NOT NULL,
  `mujeres` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_recibeninfo_24ec5559` (`informe_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_recibeninfo`
--

LOCK TABLES `contraparte_recibeninfo` WRITE;
/*!40000 ALTER TABLE `contraparte_recibeninfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_recibeninfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_referenciacontrareferencia`
--

DROP TABLE IF EXISTS `contraparte_referenciacontrareferencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_referenciacontrareferencia` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `informe_id` int(11) NOT NULL,
  `instancia` int(11) NOT NULL,
  `tipo_referencia` int(11) NOT NULL,
  `atendido_personal_pertinente` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contraparte_referenciacontrareferencia_24ec5559` (`informe_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_referenciacontrareferencia`
--

LOCK TABLES `contraparte_referenciacontrareferencia` WRITE;
/*!40000 ALTER TABLE `contraparte_referenciacontrareferencia` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_referenciacontrareferencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contraparte_tipoobservatorio`
--

DROP TABLE IF EXISTS `contraparte_tipoobservatorio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contraparte_tipoobservatorio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contraparte_tipoobservatorio`
--

LOCK TABLES `contraparte_tipoobservatorio` WRITE;
/*!40000 ALTER TABLE `contraparte_tipoobservatorio` DISABLE KEYS */;
/*!40000 ALTER TABLE `contraparte_tipoobservatorio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=130 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2011-06-09 17:41:30',1,2,'1','Contraparte',1,''),(2,'2011-06-09 17:42:07',1,2,'2','Equipo Fed',1,''),(3,'2011-06-09 17:42:24',1,3,'2','equipofed',1,''),(4,'2011-06-09 17:42:31',1,3,'2','equipofed',2,'Modificado/a is_staff y groups.'),(5,'2011-06-09 17:42:44',1,3,'3','simas',1,''),(6,'2011-06-09 17:42:51',1,3,'3','simas',2,'Modificado/a is_staff y groups.'),(7,'2011-06-09 17:43:38',2,12,'1','SIMAS',1,''),(8,'2011-06-09 17:44:13',2,16,'1234','SIMAS - 1234',1,''),(9,'2011-06-09 17:44:57',1,15,'1','Resultado 1.1',1,''),(10,'2011-06-09 17:45:11',1,15,'2','Resultado 1.2',1,''),(42,'2011-06-17 16:27:51',2,16,'2','AMNLAE- Juigalpa - FED-C20-2010',1,''),(12,'2011-06-09 17:49:58',2,16,'1234','SIMAS - 1234',2,'Modificado/a resultados.'),(14,'2011-06-09 18:02:21',2,14,'1','Prevención de la violencia de género',1,''),(15,'2011-06-09 18:02:32',2,14,'2','Salud Sexual y Reproductiva',1,''),(16,'2011-06-09 18:02:39',2,14,'3','Atención en salud a víctimas de violencia',1,''),(17,'2011-06-09 18:02:47',2,14,'3','Atención en salud a víctimas de violencia',2,'No ha cambiado ningún campo.'),(18,'2011-06-09 18:02:50',2,14,'4','VIH y SIDA',1,''),(19,'2011-06-09 18:02:58',2,14,'5','Masculinidad',1,''),(20,'2011-06-09 18:03:05',2,14,'6','Diversidad sexual',1,''),(21,'2011-06-09 18:03:28',2,14,'7','Aborto terapeutico',1,''),(41,'2011-06-17 15:23:56',2,16,'FED-C20-2010*','AMNLAE- Juigalpa - FED-C20-2010*',2,'Modificado/a codigo.'),(38,'2011-06-17 15:16:52',2,16,'FED-CP- 099-2010','AMNLAE- Juigalpa',3,''),(39,'2011-06-17 15:17:12',2,16,'FED-CP- 099-2010','AMNLAE- Juigalpa',3,''),(40,'2011-06-17 15:23:22',2,16,'FED-C20-2010','AMNLAE- Juigalpa - FED-C20-2010',1,''),(37,'2011-06-17 14:17:18',2,14,'8','Asociación  de Mujeres Nicaragüenses “Luisa Amanda Espinoza”',1,''),(36,'2011-06-17 10:40:00',2,12,'2','AMNLAE- Juigalpa',1,''),(26,'2011-06-10 16:21:36',2,20,'4','SIMAS | Período: Febrero 2011 - Julio 2011',1,''),(35,'2011-06-16 17:54:44',1,2,'2','Equipo Fed',2,'Modificado/a permissions.'),(28,'2011-06-14 17:02:12',2,15,'3','Resultado 2.1',1,''),(29,'2011-06-14 17:02:54',2,15,'4','2.2',1,''),(30,'2011-06-14 17:14:20',2,15,'4','Resultado 2.2',2,'Modificado/a nombre_corto.'),(31,'2011-06-14 17:24:41',2,15,'5','Resultado 2.3',1,''),(32,'2011-06-14 17:25:13',2,15,'6','Resultado 3.1',1,''),(33,'2011-06-14 17:26:11',2,12,'1','SIMAS',3,''),(34,'2011-06-16 17:47:20',2,3,'3','simas',3,''),(43,'2011-06-17 16:28:02',2,16,'2','AMNLAE- Juigalpa - FED-C20-2010',3,''),(44,'2011-06-17 16:50:25',2,16,'3','AMNLAE- Juigalpa - FED-CP- 099-2010',1,''),(45,'2011-06-17 16:51:43',2,16,'1','AMNLAE- Juigalpa - FED-099-2010',2,'No ha cambiado ningún campo.'),(46,'2011-06-17 16:52:15',2,16,'1','AMNLAE- Juigalpa - FED-099-2010',3,''),(47,'2011-06-17 17:17:53',2,12,'3','SI Mujer',1,''),(48,'2011-06-17 17:37:07',2,16,'4','SI Mujer - FED-AP-01-2010',1,''),(49,'2011-06-17 22:24:19',2,16,'5','AMNLAE- Juigalpa - asdfasdfa',1,''),(50,'2011-06-17 22:24:32',2,16,'5','AMNLAE- Juigalpa - asdfasdfa',2,'Modificado/a monto_fed.'),(51,'2011-06-17 22:24:39',2,16,'5','AMNLAE- Juigalpa - asdfasdfa',3,''),(52,'2011-06-20 12:54:45',2,12,'4','Dos Generaciones',1,''),(53,'2011-06-20 15:12:15',2,16,'6','AMNLAE- Juigalpa - asdfs',1,''),(54,'2011-06-20 15:12:51',2,16,'6','AMNLAE- Juigalpa - asdfs',2,'Modificado/a monto_contrapartida.'),(55,'2011-06-20 15:13:15',2,16,'6','AMNLAE- Juigalpa - asdfs',3,''),(56,'2011-06-20 15:50:39',2,16,'7','Dos Generaciones - FED-AP-04-2010',1,''),(57,'2011-06-20 15:57:22',2,12,'5','Asociación Mary Barreda',1,''),(58,'2011-06-20 16:10:29',2,16,'8','Asociación Mary Barreda - FED-016-2010',1,''),(59,'2011-06-20 16:51:52',2,12,'6','CANTERA',1,''),(60,'2011-06-20 17:12:53',2,16,'9','CANTERA - FED- 032-2010',1,''),(61,'2011-06-21 10:12:48',2,12,'7','CESESMA ',1,''),(62,'2011-06-21 10:20:00',2,16,'10','CESESMA  - FED – 076 - 2010',1,''),(63,'2011-06-21 10:31:11',2,12,'8','FECONORI',1,''),(64,'2011-06-21 11:03:36',2,14,'8','Asociación  de Mujeres Nicaragüenses “Luisa Amanda Espinoza”',3,''),(65,'2011-06-21 11:04:43',1,2,'2','Equipo Fed',2,'Modificado/a permissions.'),(66,'2011-06-21 11:05:22',2,16,'10','CESESMA  - FED-076-2010',2,'Modificado/a codigo.'),(67,'2011-06-21 11:05:34',2,16,'9','CANTERA - FED-032-2010',2,'Modificado/a codigo.'),(68,'2011-06-21 15:41:09',2,20,'5','AMNLAE- Juigalpa | Período: Febrero 2011 - Julio 2011',1,''),(69,'2011-06-21 15:42:08',2,20,'5','AMNLAE- Juigalpa | Período: Febrero 2011 - Julio 2011',3,''),(70,'2011-06-21 16:17:44',2,12,'9','CDMDM',1,''),(71,'2011-06-21 16:26:12',2,13,'1','Ayuntamiento de Donostia',1,''),(72,'2011-06-21 16:26:31',2,13,'2','Gobierno de Navarra',1,''),(73,'2011-06-21 16:27:02',2,13,'3','Central Sanitaria Suiza',1,''),(74,'2011-06-21 16:29:33',2,16,'11','CDMDM - FED – 070- 2010',1,''),(75,'2011-06-21 16:51:10',1,20,'6','SI Mujer | Período: Febrero 2011 - Julio 2011',1,''),(76,'2011-06-21 17:05:38',2,12,'10','OYANKA',1,''),(77,'2011-06-22 09:35:06',2,12,'2','AMNLAE- Juigalpa',2,'Modificado/a telefono_1.'),(78,'2011-06-22 09:41:07',2,12,'11','Los Cumiches',1,''),(79,'2011-06-22 10:36:50',2,16,'12','Los Cumiches - FED 074 - 2010',1,''),(80,'2011-06-22 10:53:29',2,16,'8','Asociación Mary Barreda - FED-016-2010',2,'No ha cambiado ningún campo.'),(81,'2011-06-22 11:02:17',2,12,'12','Grupo Venancia',1,''),(82,'2011-06-22 11:18:00',2,13,'4','MUGARIK GABE',1,''),(83,'2011-06-22 11:18:16',2,13,'5','ONE WORLD ACTION',1,''),(84,'2011-06-22 11:18:36',2,13,'6','ENTREPUEBLOS',1,''),(85,'2011-06-22 11:18:54',2,13,'7','ACSUR-Las Segovias',1,''),(86,'2011-06-22 11:19:19',2,13,'8','COOPERACCIÓ',1,''),(87,'2011-06-22 11:19:34',2,13,'9','VIENTOS DE PAZ  ',1,''),(88,'2011-06-22 11:20:21',2,13,'10','Inst de la Mujer España ',1,''),(89,'2011-06-22 11:30:40',2,16,'13','Grupo Venancia - FED-081-2010',1,''),(90,'2011-06-22 11:39:25',2,12,'13','CCBN',1,''),(91,'2011-06-22 11:46:48',2,13,'11','International Foundation',1,''),(92,'2011-06-22 11:47:59',2,13,'12','Parroquia Corazon Maria',1,''),(93,'2011-06-22 11:52:00',2,16,'14','CCBN - FED-066-2010',1,''),(94,'2011-06-22 12:06:01',2,12,'14','Movimiento Feminista de N',1,''),(95,'2011-06-22 12:28:57',2,16,'15','Movimiento Feminista de N - FED- 057-2010',1,''),(96,'2011-06-22 12:36:28',2,12,'15','AHV Colectivo Gaviota',1,''),(97,'2011-06-22 14:49:01',2,13,'13','DIAKONIA',1,''),(98,'2011-06-22 14:52:49',2,16,'16','AHV Colectivo Gaviota - FED-027-2010',1,''),(99,'2011-06-22 15:22:14',2,12,'16','FMR',1,''),(100,'2011-06-22 15:41:10',2,16,'17','FMR - FED – 122 -2010',1,''),(101,'2011-06-22 16:08:51',2,12,'17','C.A.V',1,''),(102,'2011-06-22 16:13:22',2,16,'18','C.A.V - FED- 087-2010',1,''),(103,'2011-06-22 16:21:06',2,12,'18','Movimiento de NATRAS',1,''),(104,'2011-06-22 16:24:54',2,13,'14','Trocaire',1,''),(105,'2011-06-22 16:26:44',1,20,'6','SI Mujer | Período: Febrero 2011 - Julio 2011',3,''),(106,'2011-06-22 16:29:20',2,16,'19','Movimiento de NATRAS - FED 133-2010',1,''),(107,'2011-06-23 17:18:13',2,12,'19','UCA San Ramón',1,''),(108,'2011-06-24 11:20:50',2,16,'20','UCA San Ramón - FED-061-2010',1,''),(109,'2011-06-24 11:26:17',2,13,'15','DRF',1,''),(110,'2011-06-24 11:26:44',2,13,'16','ADD',1,''),(111,'2011-06-24 11:28:05',2,13,'17','FC-Oxfam',1,''),(112,'2011-06-24 11:28:22',2,13,'18','UNICEF',1,''),(113,'2011-06-24 11:32:56',2,16,'21','FECONORI - FED-120-2010',1,''),(114,'2011-06-24 14:45:45',2,12,'20','Puntos de Encuentro ',1,''),(115,'2011-06-24 14:51:54',2,13,'19','Embajada de Noruega',1,''),(116,'2011-06-24 14:52:52',2,13,'20','Oxfam Novib',1,''),(117,'2011-06-24 14:53:22',2,13,'21','CCFD',1,''),(118,'2011-06-24 14:54:13',2,13,'22','Fondo Fiduciario/Onu Muje',1,''),(119,'2011-06-24 14:54:34',2,13,'23','Save The Children España',1,''),(120,'2011-06-24 14:54:58',2,13,'24','Broderlijk Delen',1,''),(121,'2011-06-24 14:55:12',2,13,'25','TDH Alemania',1,''),(122,'2011-06-24 14:55:30',2,13,'26','Fondo MGD3',1,''),(123,'2011-06-24 14:56:45',2,13,'27','WWB',1,''),(124,'2011-06-24 14:57:05',2,13,'28','UNICEF',1,''),(125,'2011-06-24 15:01:00',2,16,'22','Puntos de Encuentro  - FED-AP-02-2010',1,''),(126,'2011-06-24 15:11:49',2,13,'29','OPS',1,''),(127,'2011-06-24 15:17:16',2,16,'23','OYANKA - FED-007-2010',1,''),(128,'2011-06-24 15:21:41',2,12,'21','NIMEHUATZIN',1,''),(129,'2011-06-24 15:32:47',2,16,'24','NIMEHUATZIN - FED-AP-03-2010',1,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(3,'user','auth','user'),(4,'message','auth','message'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'site','sites','site'),(8,'log entry','admin','logentry'),(9,'migration history','south','migrationhistory'),(10,'departamento','lugar','departamento'),(11,'municipio','lugar','municipio'),(12,'Organización','fed','organizacion'),(13,'donante','fed','donante'),(14,'Tema de FED','fed','tema'),(15,'resultado','fed','resultado'),(16,'proyecto','fed','proyecto'),(17,'Tema de trabajo','fed','tematrabajo'),(18,'Población Meta Directa','fed','poblacionmetadirecta'),(19,'Población Meta Indirecta','fed','poblacionmetaindirecta'),(20,'informe','contraparte','informe'),(21,'accion impulsada','contraparte','accionimpulsada'),(22,'accion implementada','contraparte','accionimplementada'),(23,'Comisión','contraparte','comision'),(24,'participacion comision','contraparte','participacioncomision'),(25,'Acción de agenda','contraparte','accionagenda'),(26,'agenda publica','contraparte','agendapublica'),(27,'Tipo de Observatorio','contraparte','tipoobservatorio'),(28,'observatorio','contraparte','observatorio'),(29,'Acción de demanda','contraparte','acciondemanda'),(30,'Demanda de Justicia','contraparte','demandajusticia'),(31,'Denuncia','contraparte','denuncia'),(32,'Posee información','contraparte','poseeninfo'),(33,'Recibe información','contraparte','recibeninfo'),(34,'Prevención de VBG','contraparte','prevencionvbg'),(35,'Masculinidad Libre','contraparte','masculinidadlibre'),(36,'caso atendido','contraparte','casoatendido'),(37,'denuncia interpuesta','contraparte','denunciainterpuesta'),(38,'Atención a Mujeres','contraparte','atencionmujer'),(39,'Referencia y Contrareferencia','contraparte','referenciacontrareferencia'),(40,'Capacidad Administrativa','contraparte','capacidadadmitiva'),(41,'Medir y Reportar','contraparte','medirreportar'),(42,'Plan Estratégico','contraparte','planestrategico');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('975eb35fae63411aaf0e604a31e8c88e','ZDQ3MWIyMDEzYzRlYzZjMTUyY2JjOWFlZjIxNWQ1Zjc0NGZkYmQ4NDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2011-06-24 16:25:28'),('25d9d8ea34a28fb3cd6eb44f96c58f16','ZDQ3MWIyMDEzYzRlYzZjMTUyY2JjOWFlZjIxNWQ1Zjc0NGZkYmQ4NDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2011-06-28 16:57:04'),('cccace84af04063001303dc30a611f9d','ZDk2OTQ0YWVhMWYwY2ZhY2M4OTIyZjQwNTExNzExZTZkOTNiMmI2MTqAAn1xAS4=\n','2011-06-23 18:08:49'),('51b4ea7adc9ebcac0dacc7a283a19521','ZDQ3MWIyMDEzYzRlYzZjMTUyY2JjOWFlZjIxNWQ1Zjc0NGZkYmQ4NDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2011-06-30 19:33:26'),('69a22c3aa148144a01de54c887987564','ZDQ3MWIyMDEzYzRlYzZjMTUyY2JjOWFlZjIxNWQ1Zjc0NGZkYmQ4NDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2011-06-30 19:13:28'),('8d2424d95dc788ff564f42dd15eb16cc','ZDQ3MWIyMDEzYzRlYzZjMTUyY2JjOWFlZjIxNWQ1Zjc0NGZkYmQ4NDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==\n','2011-07-01 10:01:23'),('6113acdf38eb97dcc9154f8cd0a12b06','ZmI0ZDFjMDVmNzYyNzc2YTczOWMxMWRiYmRmZWY3YjYxY2NjNjJkNDqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVCWdyYWxfeWVhcnEESwB1Lg==\n','2011-07-11 09:44:34');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fed_donante`
--

DROP TABLE IF EXISTS `fed_donante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fed_donante` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(200) NOT NULL,
  `nombre_corto` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fed_donante`
--

LOCK TABLES `fed_donante` WRITE;
/*!40000 ALTER TABLE `fed_donante` DISABLE KEYS */;
INSERT INTO `fed_donante` VALUES (1,'Ayuntamiento de Donostia','Ayuntamiento de Donostia'),(2,'Gobierno de Navarra','Gobierno de Navarra'),(3,'Central Sanitaria Suiza','Central Sanitaria Suiza'),(4,'MUGARIK GABE','MUGARIK GABE'),(5,'ONE WORLD ACTION','ONE WORLD ACTION'),(6,'ENTREPUEBLOS','ENTREPUEBLOS'),(7,'ACSUR-Las Segovias','ACSUR-Las Segovias'),(8,'COOPERACCIÓ','COOPERACCIÓ'),(9,'VIENTOS DE PAZ  ','VIENTOS DE PAZ  '),(10,'Instituto de la Mujer de España','Inst de la Mujer España '),(11,'International Foundation','International Foundation'),(12,'Parroquia Corazón Inmaculado de María','Parroquia Corazon Maria'),(13,'DIAKONIA','DIAKONIA'),(14,'Trocaire','Trocaire'),(15,'DISABILITHY RIGHT FOUND','DRF'),(16,'ASOCIACION DANESA DE DISCAPACITADOS','ADD'),(17,'FONDO-COMUN -OXFAN','FC-Oxfam'),(18,'UNICEF','UNICEF'),(19,'Embajada de Noruega','Embajada de Noruega'),(20,'Oxfam Novib','Oxfam Novib'),(21,'CCFD','CCFD'),(22,'Fondo Fiduciario/Onu Mujeres','Fondo Fiduciario/Onu Muje'),(23,'Save The Children España','Save The Children España'),(24,'Broderlijk Delen','Broderlijk Delen'),(25,'TDH Alemania','TDH Alemania'),(26,'Fondo MGD3','Fondo MGD3'),(27,'WWB','WWB'),(28,'UNICEF','UNICEF'),(29,'Organizacion Panamericana de la Salud','OPS');
/*!40000 ALTER TABLE `fed_donante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fed_organizacion`
--

DROP TABLE IF EXISTS `fed_organizacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fed_organizacion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `nombre_corto` varchar(25) NOT NULL,
  `direccion` varchar(250) NOT NULL DEFAULT '',
  `fecha` date NOT NULL DEFAULT '2011-06-08',
  `no_mingob` varchar(50) NOT NULL DEFAULT '',
  `no_ruc` varchar(50) NOT NULL DEFAULT '',
  `no_inss` varchar(50) NOT NULL DEFAULT '',
  `representante_legal` varchar(120) NOT NULL DEFAULT '',
  `email` varchar(75) NOT NULL DEFAULT 'email@example.com',
  `contacto` varchar(120) NOT NULL DEFAULT '',
  `telefono_contacto` varchar(15) NOT NULL DEFAULT '',
  `sitio_web` varchar(200) NOT NULL DEFAULT 'www.example.com',
  `obj_gral` longtext NOT NULL,
  `estrategias` longtext NOT NULL,
  `antecedentes` longtext NOT NULL,
  `telefono_1` varchar(15) NOT NULL,
  `telefono_2` varchar(15) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fed_organizacion_fbfc09f1` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fed_organizacion`
--

LOCK TABLES `fed_organizacion` WRITE;
/*!40000 ALTER TABLE `fed_organizacion` DISABLE KEYS */;
INSERT INTO `fed_organizacion` VALUES (2,1,'Asociación  de Mujeres Nicaragüenses “Luisa Amanda Espinoza”','AMNLAE- Juigalpa','De ENITEL 1c Norte, Juigalpa Chontales.','1990-03-30','124','2909779505','233957','María del Socorro Méndez','juigalpaamnlae@yahoo.es','María del Socorro Méndez.','2512- 2741','http://WWW.amnlaenicaragua.org.ni/','Lograr le trasformación de las relaciones desiguales de poder entre mujeres y hombres en el ámbito público y privado, promoviendo un nuevo liderazgo desde las mujeres, que les permita hacer uso consciente de sus derechos de ciudadanía plena, para con','1.- Lucha Contra la Violencia de Género.\r\n2.- Poder y Liderazgo.\r\n3.- Salud Integral.\r\n4.- Autonomía Económica y Medio Ambiente.\r\n5.- Desarrollo Integral de adolescentes y Jóvenes.\r\n','AMNLAE tiene un plan estratégico que cuenta con grandes líneas generales como la prevención y atención de la violencia basada en género, también realizan actividades dirigidas a la atención y demanda de justicia para las víctimas de violencia intrafamiliar y sexual, mediante la incidencia para que se aplique los protocolos de actuaciones, e integrarse en espacios de incidencia local y departamental. Además contribuye a fortalecer el modelo de atención a víctimas de VIF y sexual para que se apliquen los protocolos de actuaciones. ','2512-2353',''),(3,1,'Asociación Servicios Integrales para la Mujer','SI Mujer','De la Estatua de Montoya 1cuadra arriba.','1991-02-11','133','110291-9609','288365','Reyna Xiomara Luna Doña','direccion@simujer.org.ni','Ana María Pizarro','2268-0038','','SI Mujer es una organización sin fines de lucro, integrada por un grupo de mujeres y hombres comprometidos con la defensa de los derechos de las mujeres adolescentes y jóvenes de ambos sexos, particularmente en el ámbito de la sexualidad y de la salud reproductiva, con especial atención a las personas más pobres. Es un centro alternativo feminista, independiente de gobiernos, partidos políticos y denominaciones religiosas, que brinda sus servicios sin discriminación de ninguna clase, con alta calidad y respeto por las usuarias y usuarios y que defiende el  derecho de las mujeres a estar informadas y a decidir sobre su propio cuerpo con libertad.','•	Políticas de Salud, Población y Desarrollo.\r\n•	Salud Sexual y Salud Reproductiva\r\n•	Derechos Sexuales y Derechos Reproductivos\r\n•	Prevención y Atención de la Violencia Sexual e Intrafamiliar.\r\n•	Prevención y Atención de la ITS/VIH/SIDA.\r\n•	Adolescencia\r\n','SI Mujer ha ejecutado desde 1991 proyectos institucionales, vinculados directamente a su Plan Estratégico y en correspondencia que contempla el desarrollo de actividades encaminadas al cumplimiento de su misión y visión y en cuyo desarrollo  participa el personal de las diferentes áreas, promotoras y promotores.','2268-0038',''),(4,1,'Centro Nicaragüense de Promoción de la Juventud y la Infancia','Dos Generaciones','Costado Oeste del Templo Mormón, Las Palmas. Managua','1990-03-20','683','200390-9835','29459-5','Mariana de Jesús Aburto Chavarría','direccion@dosgeneraciones.org','Mario Ernesto Chamorro Ruíz','2266-4999','http://www.dosgeneraciones.org/','Niñas, niños, adolescentes y jóvenes de Nicaragua gozan y ejercen plenamente sus derechos. ¡Niños Felices!.','1.	Educación, \r\n2.	Salud, \r\n3.	Protección Integral, \r\n4.	Seguridad Económica\r\n','El Centro Nicaragüense de Promoción de la Juventud y la Infancia “Dos Generaciones” está constituido  como una asociación de carácter civil, no gubernamental, sin fines de lucro desde el 20-Marzo-1990, está presente desde 1992 en siete sectores del Barrio Acahualinca en Managua, el que cuenta con una población de aproximadamente de 10,324 habitantes. En un primer momento realizó intervención social con niñas, niños y adolescentes trabajadores de La Chureca, y para el 2007 su trabajo social adquiere un enfoque de desarrollo humano desde la comunidad, planteándose 4 componentes: Educación, Salud, Protección Integral y Seguridad Económica, teniendo como ejes transversales género, participación comunitaria y comunicación social. Nuestro grupo meta es la población de estos sectores, en particular las niñas, niños, adolescentes, jóvenes y mujeres.','2266-4960',''),(5,1,'Asociación Civil Particular Proyecto Mujer Mary Barreda','Asociación Mary Barreda','Iglesia La Recolección 1/2c. arriba','1989-09-05','292','101293-9546','37536-0','Zela Mauricia Díaz Valle','marybarredaleon@yahoo.com','Mercedes del Socorro Toruño T.','2311-2259','http://www.asociacionmarybarreda.com.org/','Contribuir al establecimiento de una realidad municipal, departamental y nacional en la que el estado y sociedad civil asumiendo responsabilidades, tienen como centralidad del desarrollo la persona humana garantizando medidas de apoyo preventivas y de protección especial a víctimas de Explotación Sexual Comercial, Trabajo Infantil de Alto Riesgo, Violencia Intrafamiliar y Sexual y Prostitución.','1.Promover la Atención individual y grupal con niñas, adolescentes y mujeres víctimas de violencia sexual para favorecer su proceso de recuperación emocional mediante el desarrollo de capacidades y la reconstrucción de su integridad hasta lograr el empoderamiento necesario para tomar decisiones autónomas en sus vidas.\r\n2. La promoción de la Movilización Social y con ella la construcción del soporte social de los Facto res Protectores Comunitarios con énfasis en el ejercicio de ciudadanía mediante la denuncia, la defensoría social y el control social.\r\n3.La promoción de la participación de las sujetas en forma activa, directa y propositiva en espacios y formas organizativas  propias, tanto en espacios locales, intermunicipales y nacionales.\r\n4.-El desarrollo de la comunicación social tanto con medios modalidades de la institución, como estimulando el desarrollo de modalidades de las sujetas y de la población.\r\n','Mary Barreda cuenta con un financiamiento por parte de FED que marcó un hito en su actuar institucional ya que le permitió el cumplimiento de lo planteado en su Plan Estratégico en relación a asumir los retos en el año 2006 con DDSS y DDRR teniendo como punto de partida un profundo proceso de reflexión, capacitación y sanación de todos sus recursos humanos y que nos permite contar con un Manual de capacitación.','2311-2259',''),(6,1,'Centro de comunicación y Educación popular - CANTERA','CANTERA','De plaza el sol, dos cuadras al sur, 1 cuadra arriba. Casa #8','2010-03-09','87','090390-9617','270132','Anabel Torres','cantera@ibw.com.ni','Linda Rene Núñez Calderón','2277-5329','http://www.canteranicaragua.org/','Contribuir al desarrollo de la conciencia crítica, la capacidad de análisis, la innovación y el compromiso social de los sectores a quienes acompañamos para la transformación de su realidad.','1.	Educación Popular: Educación crítica, cuestionadora y reivindicativa de la realidad.\r\n2.	Género: De-construcción de la cultura e identidad patriarcal tanto de parte de los hombres como de las mujeres, construcción de nuevas relaciones de equidad y compromiso político para transformar la realidad.\r\n3.	Espiritualidad y ética: Transformación personal y comunitaria para el rescate de la identidad y los  valores, partiendo de una visión holística de la realidad, creando el equilibrio entre el cuerpo y el espíritu, entre la persona y la naturaleza, entre los sueños y la realidad que buscamos transformar. \r\n4.	Salud Comunitaria y medio ambiente: Adopción de nuevas prácticas higiénico-sanitarias y formas de ejercer la soberanía ambiental y el equilibrio ecológico.\r\n5.	Incidencia: Capacidad de gestión y transformación a partir de la participación activa en los  procesos organizativos  locales, municipales y nacionales.\r\n','CANTERA es una organización nicaragüense no gubernamental, de tipo humanitario, sin fines de lucro y con personería jurídica propia. La institución está al servicio del desarrollo integral de los sectores populares del campo y la ciudad.  \r\nCantera fue fundada en el año 1988. Cuenta con acta de fundación y estatutos aprobados por el gobierno de Nicaragua. \r\nCantera es miembro de la Coordinación Centroamericana de Educación Popular Alforja, del Consejo de Educación de Adultos de América Latina (CEAAL) y de la Federación de Organismos No Gubernamentales de Nicaragua. También participa de diversas redes, tanto nacionales como regionales, relacionadas con el trabajo de los distintos programas que se desarrollan en el Centro.\r\n','2278-0103',''),(7,1,'Centro de Servicios Educativos en Salud y Medio Ambiente  ','CESESMA ','Alcaldía de San Ramón 1 C al Sur, ½ C al Oeste ','1999-08-05','1308','NIT:J0110000014710','335216','Guillermo José Medrano ','coordinacion@cesesma.org','Marisol Hernández Méndez ','2772 - 5660','http://www.cesesma.org/','Contribuir a la promoción y defensa de los derechos de la niñez y la adolescencia. ','Formación, organización, desarrollo y fortalecimiento de redes de promotores niños, niñas y adolescentes que incluye: \r\na)	Formación y capacitación de promotores y promotoras educativos comunitarios.\r\nb)	Organización de niños, niñas y adolescentes para la incidencia en la familia, la escuela y comunidad. \r\n•	Economía familiar, cultivo de patio con técnicas agroecológicas \r\n•	Desarrollo artístico y manualidades \r\n•	Desarrollo de actividades vocacionales \r\n•	Comunicación social (teatro, animación y promoción de lectura, radio)\r\nc)	Desarrollo y fortalecimiento de redes conformadas por niñas, niños y adolescentes. \r\nIncidencia en instancias municipales, departamentales y nacionales\r\nFormación y capacitación de personas adultas (incluye, madres, padres, líderes, liderezas, docentes, autoridades locales) \r\nComunicación institucional\r\n','CESESMA surgió en 1996 resultado del crecimiento y éxito de un programa de educación en salud para niños y niñas que comenzó en 1992 en el municipio de San Ramón – departamento de Matagalpa. A partir de esta experiencia, se conformó un equipo de trabajo y el programa fue ampliado a mayor número de escuelas y comunidades rurales, facilitando la capacitación a docentes, líderes comunitarios, padres, madres, niños, niñas y adolescentes en temas relacionados a identidad, género, salud preventiva y medio ambiente. \r\n\r\nLa experiencia de trabajo trascendió al ámbito de la educación formal con perspectiva de desarrollo comunitario con énfasis en la promoción y defensa de los derechos de la niñez, promoviendo la participación de niños, niñas y adolescentes sin acceso a la educación formal e incorporando a grupos de padres, madres, líderes y docentes y estableciendo sinergias a través de coordinaciones y alianzas establecidas desde espacios locales, nacionales e internacionales. \r\n','2772 - 5660',''),(8,1,'Federación Nicaragüense de Asociaciones de Personas con Discapacidad ','FECONORI','De  la óptica Nicaragüense 1 cuadra arriba  1 cuadra al sur ','1994-01-01','1390','220998-9517','602359-12','David López  Ordoñez','Feconori01@yahoo.es','Alma Nubia Baltodano','2268-1564','http://www.discapacidad-ca.org/feconori','Promover la defensa de los derechos humanos  de las personas con discapacidad a fin de que puedan optar en igualdad de condiciones y oportunidades para un mejor nivel de vida.','Línea estratégica 1: Incidencia permanente y sistemática ante el Estado y Sociedad Civil en general\r\n\r\nLínea estratégica 2: Fortalecimiento organizativo de FECONORI\r\n\r\nLínea estratégica 3:\r\nFortalecimiento Institucional de FECONORI\r\n','La Federación Nicaragüense  de Asociaciones de personas con discapacidad FECONORI aglutina a 20 asociaciones de personas con discapacidad de todo tipo: sensoriales, físicos y mentales. \r\nLa mayoría de ellas tienen su Personería Jurídica y 8 de ellas son expresiones de cobertura nacional  y las otras de expresiones municipales \r\n\r\nDesde el año 2008  la Feconori inicia un proceso de recuperación desde el ámbito institucional hasta de ir recuperando su papel en  liderar  procesos de lucha del  sector de PCD, en primera instancia nos propusimos elaborar un Plan Estratégico 2008 -2013  y debido a su cumplimiento,   en octubre del 2010  se tuvo que realizar evaluación y reformulación de un nuevo plan 2011-2015 \r\n\r\nLa FECONORI desde febrero del 2009 cuenta con independencia administrativa, y a pasado de tener un donante en 2008 cuenta a  4 donantes en el 2010 , el 80 % de sus socios participan activamente en sus principales acciones , es reconocida en las instituciones del Estado , Ejecutivo, Legislativo, MINED,MIFAMILIA,INATEC,MITRAB.\r\n\r\nLa FECONORI cuenta dentro de sus estructuras con una asamblea general en la que participan los socios de la federacion y es la màxima autoridad esta se reune cada seis meses, la Junta directiva Nacional se reune bimensualmente, actualmente se han formado 7 filiales a nivel municipal con las organizaciones presentes en las localidades y en 4 muncipios estan constituidos núcleos  que son la ante sala de la formacion de las filiales.\r\n\r\nLas filiales de la federacion en las localidades son sumanente  importantes para lograr una incidencia eficaz y pertinente en las localidades  , para la ejecucion de sus planes la FECONORI cuenta con 4 comisiones de trabajo ,Comision Juridica, Comision de accesibilidad,Comision de Rehabilitacion y Comision de Educacion ,a estas comisiones participan las diferentes asociaciones segun sus intereses \r\n','2268-1564',''),(9,1,'Colectiva de Mujeres de Masaya','CDMDM','Enitel 1 cuadra al norte, Masaya','1995-02-16','595','160295 - 9569','37601 - 2','Clemen Lorena Altamirano Carcache','email@example.com','Ericka Vanessa Tórrez Tellería','2522 – 5458   ','http://www.wix.com/mujer_y_salud/colectiva-de-mujeres-de-masaya','Fortalecer las estrategias de empoderamiento de las mujeres para el ejercicio de sus derechos humanos y su ciudadanía a través de su participación organizada.','1.	Lucha contra la violencia hacia las mujeres\r\n2.	Promoción de los derechos sexuales y derechos reproductivos\r\n3.	Derecho a la educación de las adolescentes, jóvenes y mujeres adultas. \r\n4.	Fortalecimiento del liderazgo individual y colectivo de las mujeres\r\n5.	Desarrollo organizacional de la Colectiva\r\n6.	Aseguramiento de recursos para el Plan Estratégico 2010-2013.\r\n','La Colectiva de Mujeres de Masaya, nace hace 17 años, como una organización sin fines de lucro con la misión de contribuir a la organización del movimiento de mujeres como movimiento autónomo democrático y plural, así como fortalecer la capacidad propositiva del mismo, para transformar las relaciones desiguales de poder entre hombres y mujeres.\r\nDicha transformación incluye que las mujeres nos apropiemos de nuestro cuerpo y nos autoafirmemos en nuestras capacidades y potencialidades, que cuestionemos todas las relaciones de poder existentes tanto a nivel estructural como en nuestra cotidianidad. \r\n','8856-4669','2522 – 5458   '),(10,1,'Asociación de Mujeres de Jalapa contra la Violencia Oyanka, Jalapa Oyanka.','OYANKA','Contiguo a Banco ProCredit, Jalapa, Nueva Segovia','1997-09-12','1260','120997-9558','36558-5','María Elena Rivera','Oyanka2@yahoo.com','Elgin Elizabeth Morales','8854-1668','http://www.oyanka.org/','Proporcionar asesoría jurídica y acompañamiento legal a mujeres, niñas y adolescentes afectadas por violencia intrafamiliar en el municipio de Jalapa, tanto en el área rural como urbana.','1.	La prevención de la violencia\r\n2.	Defensa y promoción de los derechos humanos de las mujeres, adolescentes y la niñez.\r\n3.	Fortalecimiento institucional\r\n4.	Incidencia política\r\n','Oyanka nace el 8 de marzo de 1993, como un programa de la mujer campesina de la cooperativa de conjuntos campesinos activos de Jalapa (CCAJ), con el objetivo de   dar atención a la problemática de las mujeres socias de las 8 cooperativas que en aquel entonces conformaban la cooperativa.\r\nDespués de conocer la problemática de las mujeres mediante una convivencia permanente en el campo, decidimos trabajar  no solamente con las mujeres cooperadas  como lo había orientado la CCAJ (previa aprobación del consejo de administración) si no con todas las mujeres que querían organizarse. Dentro de los principales problemas que se detectaron que vivían las mujeres fueron: problemas económicos, porque las mujeres estaban siendo despojadas de sus tierras y sus créditos por parte de los mismos socios de la CCAJ, problemas de violencia intrafamiliar y sexual y problemas de salud.\r\nEl tener contradicciones con los directivos y socios de la CCAJ nos llevó a pensar en una independencia y en formar una organización autónoma de las mujeres que defendiera nuestros derechos. Al finalizar el año 96 mediante una consultoría financiada por HIVOS, se definió el papel dentro de la CCAJ, así como la independencia del área legal, tomando como punto de partida que en la evaluación realizada una de las principales fortaleza de CCAJ. Era el trabajo por la defensa de los derechos de las mujeres.\r\nLuego de la consultoría, se comienza con proceso  de consulta con todas las mujeres del campo, lo que dió como resultado que el 12 de Septiembre del año 1997 nos constituyéramos como la Asociación de Mujeres de Jalapa contra la violencia OYANKA, y surge con el objetivo de disminuir el índice de violencia en el Municipio.\r\n','2737-2360',''),(11,1,'Asociación de Comunicación y Movilización Social “Los Cumiches”','Los Cumiches','Ministerio de Gobernación ½ Cuadra el este','1998-12-10','1523','051298-9519','415935-2','Guiomar Irías','loscumiches@yahoo.es','Ramón Ordóñez','2713 - 5443','http://www.radiocumiches.com/','Defender y Promover, a través de estrategias de comunicación y movilización social, los derechos de las niñas, niños, adolescentes y jóvenes contribuyendo al mejoramiento de su entorno social y condiciones de vida.','Capacitación a:\r\n•	Niños, Niñas y Adolescentes y jóvenes\r\n•	Maestros\r\n•	Madres y padres de familia\r\nComunicación:\r\n•	Producción, transmisión de programas radiales, campañas de sensibilización, consultas.\r\nMovilización:\r\n•	Organización de redes y trabajo Interinstitucional en  función del cumplimiento de los derechos de la niñez y adolescencia.\r\nEducación no Formal: \r\nA través de metodologías de aprendizaje no formales  con los principales actores, viviendo procesos de crecimiento personal con las/os comunicadores niñas, niños y adolescentes y jóvenes.\r\n','Los Cumiches nace el 16 de Agosto de 1991 como un programa infantil de niños/as, para niños/as, y elaborados por niños/as, y que se trasmitía 1 hora, 1 vez a la semana. Su objetivo fue la promoción y divulgación de los derechos de la niñez. Se organizó una red de corresponsales que apoyados por un grupo de facilitadoras/es generaron un proceso de reflexión sobre los derechos de la niñez  y desde el programa radial se promovía el conocimiento de los mismos hacia las niñas/os de Estelí.\r\nEn Agosto de 1996, se funda Radio Cumiches como una emisora, trasmitiendo en los 107.7 FM con una programación de 8 horas diaria con distintos programas radiales, donde se le daba la oportunidad a las niñas y niños, adolescentes y jóvenes a hacer uso del derecho a la libertad de expresión y ellos podían demandar el cumplimiento de sus derechos.\r\nEn el mes de Diciembre del año 1998, se constituye legalmente la Asociación de Comunicación y Movilización Social los Cumiches como una Asociación sin fines de lucro, \r\nLa Asociación los Cumiches, es miembro de la  coordinadora de ONG´S que trabaja con la niñez y la adolescencia, la Red Nacional de Comunicadores Infantiles, y también de la Comisión de la Niñez y la adolescencia del municipio de Estelí. Nuestra Emisora, Radio Cumiches está afiliada a la Asociación mundial de Radios Comunitarias  AMARC.\r\nEn el 2009 - 2010 FAO y Radio Cumiches capacita y forma la red de jóvenes comunicadores rurales con 150 miembros/as para la promoción del tema de seguridad alimentaria y nutricional en 21 municipios de la zona seca del país (Estelí, Madriz, Nueva Segovia)','2713 - 5443',''),(12,1,'Asociación Civil  Grupo Venancia','Grupo Venancia','De la ermita Guadalupe 1 ½ c. al sur. Barrio Guanuca,  Matagalpa','1993-03-08','300 ','0803939578','32463 - 2','María de la Paz Aráuz Picado','venancia9@turbonett.com','Maria Eugenia Gómez López','2772 – 3562    ','http://www.grupovenancia.org/','Aportar a la construcción de relaciones equitativas entre mujeres y entre mujeres y hombres, promoviendo valores y prácticas no discriminatorias  y  el empoderamiento personal y colectivo de las mujeres.','a-	FORMACIÓN, ORGANIZACIÓN Y ATENCIÓN\r\nLínea Operativa 1: Procesos de formación\r\nLO 2:  Procesos de fortalecimiento organizativo\r\nb-	PROMOCION CULTURAL\r\nLO 4: Programa Radial La Hora Lila\r\nLO 5: Centro Cultural Guanuca\r\nc-	INCIDENCIA\r\nLO 7: Campaña de sensibilización\r\nd-	FORTALECIMIENTO INSTITUCIONAL\r\nLO 10: Recursos humanos\r\n','Grupo Venancia es una organización de Educación y Comunicación Popular Feminista ubicada en Matagalpa en la región centro-norte de Nicaragua. \r\nNacimos en 1991  con el propósito de ejercer libremente nuestra combinación de conocimientos en metodología y feminismo, para aportar a la construcción de un movimiento de mujeres, entre mujeres urbanas y rurales, chavalas y no tan chavalas, fortaleciendo la autonomía y el crecimiento personal desde nuestras diversas identidades e individualidades.  \r\nEl Grupo Venancia nace con el propósito de contribuir al desarrollo del movimiento de mujeres en Nicaragua. Desde los primeros planteamientos nos propusimos contribuir a esta construcción con una visión de autonomía, de integración de mujeres urbanas y rurales, jóvenes y adultas y de confluencia de la diversidad de identidades.\r\nPartimos del convencimiento que para impulsar transformaciones sociales y culturales era necesario darnos espacios para los procesos de cambio y transformación personal. Y que para sostener este proceso de cambio personal, necesitamos de espacios colectivos donde integrarnos para construir complicidad con otras mujeres y actuar juntas.\r\nA la vez, veíamos como reto que el desarrollo de este movimiento estuviera marcado también por la búsqueda de nuevas formas de organización, coordinación,  articulación y relación coherentes con la crítica al poder patriarcal y a las formas organizativas jerárquicas en las que se expresa.\r\nCon estos principios hemos sido parte de este creciente, diverso, activo y beligerante movimiento y hemos participado a lo largo de estos casi veinte años en distintos espacios de articulación, iniciativas y procesos orientados a fortalecer a las mujeres como un movimiento social beligerante, comprometido en la defensa de los derechos de todas las mujeres.\r\nActualmente formamos parte de la Red de Mujeres de Matagalpa, de la Red de Mujeres del Norte Ana Lucila y de la Red de Mujeres contra la Violencia. A nivel centroamericano formamos parte de la Alianza Feminista Centroamericana por la Transformación de la Cultura Patriarcal.\r\n','2772-3562','8944-8146'),(13,1,'Asociación Centro Cultural Batahola Norte','CCBN','Bo. Batahola Norte, de donde fue la embajada de EEUU, 1 cuadra Al oeste, 3 cuadras al norte, 1 cuadra al oeste, Managua. ','2009-02-17','4466','151105-9468','63683-7','Sonia del Carmen Olivares Rivas ','jennifer@centrobatahola.org','Darling Munguia Garcia ','22504542','','El CCBN brinda oportunidades y espacios para niñas, niños, adolescentes y jóvenes de ambos sexos y mujeres adultas de bajos recursos económicos para estudios básicos, técnicos, artísticos y culturales, para acceder a la educación formal y no formal.','-	Realizar actividades (por ejemplo, campanas) de sensibilización para que los cursos sean atractivos para mujeres y hombres, independientemente de su asociación tradicional de género.\r\n-	La Selección de becados y becadas internas y externas, debe asegurar que sean otorgadas a personas de escasos recursos. \r\n-	Implementar cursos de educación básica para adultos/as (alfabetización y ciclo de primaria).\r\n-	Implementar cursos de formación artística (danza, música, pintura y teatro).\r\n-	Implementar Charlas, talleres y capacitaciones vivenciales, de género y de los derechos humanos universales, de la mujer y la niñez, para padres, madres y estudiantes.\r\n','El Centro Cultural Batahola Norte (CCBN) es un centro comunitario de educación y arte, fundado en 1983 para acompañar a las mujeres, niños y niñas de los barrios populares y marginados de Managua en su búsqueda de nuevas y más dignas formas de vida.  La misión  del CCBN es “Vivir un estilo de vida más fraterno y justo, según el evangelio y partiendo de los pobres, a través de la cultura y la educación integral, que hacen descubrir los derechos humanos, la autoestima y la igualdad”. El CCBN está abierto a todos sin distinción de religión, credo o raza, con valores arraigados en la fe cristiana de sus fundadores, el Padre Ángel Torrellas, OP (QEPD) y la Hermana Margarita Navarro, CSJ (QEPD).\r\n\r\nLa prioridad del CCBN es aumentar la independencia económica de los adultos y enriquecer la educación y resiliencia psicosocial de los niños, niñas y adolescentes a través del arte, la cultura y el apoyo académico.  Entre sus programas se cuenta con un Área de Docencia que capacita a más de 700 personas cada año, una Biblioteca de 5,000 libros accesible a la comunidad, un coro y una orquesta juvenil, grupos de baile folklórico y teatro, un programa de becas que ayuda a 225 jóvenes y mujeres para que sigan estudiando y desarrollen su compromiso social y un programa de prevención de la violencia hacia mujeres, niños y niñas que trabaja con la población estudiantil del CCBN y en el Barrio Jorge Dimitrov.\r\n','2250-4542',''),(14,1,'Asociación programa Regional Feminista , MFN-La Corriente','Movimiento Feminista de N','Del Canal 10,  1 ½ cuadra al norte, Barrio Marta Quezada, Managua','2006-01-01','757','2510959470','33766-7 ','María Teresa Blandón Gadea','mfeminista@cablenet.com.ni','Mirna Blandón Gadea','2222-4803 ','http://www.movimientofeministanicaragua.org/','Fortalecer este espacio de articulación feminista como expresión de ejercicio de la ciudadanía de las mujeres, para la defensa de los  derechos sexuales y reproductivos de las mujeres.','1.	Contribuir con el empoderamiento de las Mujeres desde el estudio de la teoría feminista desmontando ideas opresivas sobre las mujeres y otros grupos discriminados.\r\n2.	Defensa del Estado Laico.\r\n3.	Construcción de la Ciudadanía activa de las Mujeres\r\n4.	Defensa del aborto y del aborto terapéutico.\r\n5.	Lucha contra otras formas de discriminación sustentadas en ideologías racistas y heteronormativas (aquí obviamente se incluye la defensa de los Derechos Sexuales y Derechos Reproductivos).\r\n','El Movimiento Feminista es una expresión del movimiento social de mujeres de Nicaragua. Este espacio feminista es el resultado de un largo proceso de reflexión, organización y participación que se expresa en la construcción de diversas plataformas políticas que reivindican derechos de las mujeres en todos los ámbitos de nuestras vidas. \r\nEs un Movimiento Social que considera criterios de diversidad y multiplicidad de miradas que implican, entre otros:\r\n•	Multi indigenismo\r\n•	Interculturalidad\r\n•	Diversidad sexual\r\n•	Prostitución.\r\n•	Intergeneracional\r\n\r\nDurante los últimos cuatro años esta diversidad de organizaciones y espacios de articulación  del mm/f  no solo han sostenido la labor que venían desarrollando en  años anteriores para la defensa de los derechos de las mujeres, sino que ha ampliado temas de intereses y diversificado estrategias para la acción pública. \r\nDesde nuestras organizaciones y como Movimiento Feminista construimos alianzas específicas con diversos actores sociales, entre los que destacamos al  Grupo De Alianza Estratégica para la Defensa del Aborto Terapéutico, espacio que contribuimos a fundar en el contexto de la penalización de aborto terapéutico por parte del gobierno de Nicaragua. Así también mantenemos coordinaciones estrechas con la Red de Mujeres Contra la Violencia en contra de las Mujeres,  a nivel local y nacional, lo que continúa  siendo una prioridad  para el fortalecimiento de las acciones colectivas.','2222-5355 ',''),(15,1,'Asociación por la Humanización de la Vida - Colectivo Gaviota','AHV Colectivo Gaviota','Carretera Masaya Km 12.3 (2° Entrada Esquipulas) 600 varas / Este, Portón Gaviota','1990-03-16','795','160796-9562','357665 ','Lucía Alicia Grilli Peral','Gaviota.nicaragua@hotmail.com','Lucía Alicia Grilli Peral','8855-3660','','Contribuir a desarrollar procesos de cambios en las relaciones entre hombres y mujeres en los distintos ámbitos de la vida social, familiar, política y económica, que garanticen el acceso a sus derechos de humanas y humanos con igualdad de género.','1.	Investigación: es la base de todas las acciones, se realizan: diagnósticos sobre problemáticas y zonas específicas, investigaciones de impacto y académicas. \r\n2.	Defensoría: consiste en un proceso de acompañamiento emocional y jurídico que incluye las actividades de escucha, asesoría, atención jurídica y emocional a mujeres víctimas de violencia, coordinación interinstitucional, mediación extrajudicial para impulsar a mujeres en el ejercicio y defensa de sus Derechos de Humanas. \r\n3.	Sensibilización: desarrolla procesos de sensibilización que propician un espacio de reflexión, análisis e intercambio entre mujeres y hombres sobre género, identidad y relaciones de poder que permita la articulación individual y colectiva de propuestas de cambio capaces de contribuir a relaciones justas de género. \r\n4.	Capacitación: se desarrollan procesos de formación y actualización en materia de DDHH con enfoque de Género y en las habilidades requeridas para la formulación, gestión y ejecución de Proyectos. \r\n5.	Acompañamiento metodológico: desarrolla asesorías y metodologías de apoyo a Organizaciones e Instituciones que precisan introducir la perspectiva de Género a lo interno o mejorar su desempeño institucional (fortalecimiento institucional). \r\n6.	Incidencia: entiende la incidencia como la suma de procesos para definir políticas y leyes (Derecho Positivo y Derecho Consuetudinario) para la equidad y también la suma de procesos dirigida a cambios que incorporen relaciones más equitativas en la toma de decisiones personales e interpersonales. \r\n','Gaviota  es una organización no gubernamental fundada en el año 1996, se conformó sobre una experiencia previa como asociada de CIAM (organización de origen mexicano) en la RAAN. La línea de vida de Gaviota se justifica en la promoción y defensa de los Derechos de las Humanas; habiendo sido la primera ONG que abordó esta temática en la Región Caribe de Nicaragua, realizando investigaciones sobre la situación de los Derechos de las Humanas y capacitando a los incipientes movimientos de mujeres que se conformaron en la región.\r\nA nivel institucional, Gaviota se extendió en los Municipios de Puerto Cabezas, Rosita y Nueva Guinea, su clave de desarrollo fueron las Defensorías, que consiste en un proceso de atención y acompañamiento a mujeres con derechos vulnerados en el marco de la Estrategia Institucional de Derechos de las Humanas.  \r\nA partir del año 2008 Gaviota prioriza en su accionar el trabajo de promoción de los Derechos de las Humanas y su visibilizacion en el Derecho Positivo o Estatal y Derecho Consuetudinario o Indígena así como los instrumentos jurídicos que garantizan su ejercicio y defensa. Es a partir de este año que se dispone a:\r\n•	Capacitación y consolidación de la Red de Brigadistas Comunitarios en el Municipio de Puerto Cabezas (600 mujeres y hombres), con capacidades locales para la promoción de los derechos de las mujeres y los instrumentos jurídicos existentes en la región (Positivo y Consuetudinario) que garantizan su acceso, de acuerdo a las particularidades de la realidad rural y multicultural de la región. \r\n•	Promover el debate comunitario sobre temas de género, incidiendo en la definición de políticas públicas que contribuyan a su consecución.\r\n•	Contribuir a que las autoridades comunales (Wihtas y Consejo de Ancianos) visibilicen los derechos, tanto colectivos como individuales, de las mujeres indígenas en el marco del Derecho Positivo y Derecho Consuetudinario.\r\n•	Promoción de mecanismo de coordinación (Cadena de Legalidad Jurídica) entre las autoridades del derecho consuetudinario y estatal, que facilite y agilice la Ruta de Acceso a la Justicia de las mujeres víctimas de violencia. \r\n','2255-0245',''),(16,1,'Fundación Mujer Rural','FMR','Frente Acodep, Jinotepe, Carazo. Nic.','2001-11-03','2437','031101-9058','46446-1','Alicia Serrano Briceño','mujer_rural@hotmail.com','Alicia Serrano Briceño','2532-1230','','Mejorar la condición  y posición de las mujeres,  jóvenes y adolescentes rurales, para fortalecer  la capacidad de autogestión, auto sostenimiento y autonomía económica  para la generación  de Ingresos a través de programas y proyectos, mejorando la salud preventiva (sexual y reproductiva) fortaleciendo los derechos sexuales y derechos reproductivos, contribuyendo a la reducción de los niveles de violencia sexual e intra familiar. Contribuir en el proceso de alfabetización y educación de adultos, fortaleciendo la educación y cultura con énfasis en jóvenes, hombres y mujeres, para promover el acceso a sus derechos.','•	Programa Económico: Producción de Alimentos (huertos, patios), Pequeña  agroindustria rural casera,  Pequeños negocios, Capacitación (Contabilidad y Administración desde la perspectiva de género), Crianza de Animales Menores. \r\n•	Programa Acceso A La Educación: Educación de Adultos,  Alfabetización.\r\n•	Programa Justicia,  Educación Y Cultura  Jurídica: Asesoría, Asistencia Legal  para la reducción de la Violencia Intra familiar contra las mujeres y la niñez en la zona rural y trabajo notarial en todas las ramas  del derecho, Atención Legal y Sicosocial a mujeres y adolescentes víctimas de la violencia intra familiar. \r\n•	Programa Salud Preventiva: Salud Sexual y Salud Reproductiva, Derechos Sexuales y Derechos Reproductivos, Prevención de la  Violencia Intra familiar.\r\n•	Programa Acceso de la Mujer a un Medio Ambiente Sano: Educación y Divulgación Ambiental, Viveros de Biodiversidad Flora y Energía, Producción Forestal Energética, Reproducción de plantas productoras de leña ornamentales y de flores en peligro de extinción Huertos de  autoconsumo, Atención a focos de Contaminación.\r\n\r\nLa estrategia a desarrollar en cada programa /proyecto está con tres ejes transversales o líneas generales.\r\nCoordinaciones Interinstitucionales, Sensibilización Social y Divulgación con metodología participativa y La Movilización y Participación Ciudadana. \r\n','La Fundación de “Mujeres Rurales” es un Organismo No Gubernamental, sin fines de lucro, fundada en el año 2001, como una alternativa que combina la atención de las  necesidades prácticas más inmediatas dirigidas a mejorar las condiciones de la mujer, con sus intereses estratégicos para mejorar  su posición  a fin de que lleguen a una ubicación más equitativa en la sociedad.\r\nLa Fundación de Mujeres Rurales es un organismo, que promueve el desarrollo de la mujer y la familia nicaragüense en los diferentes sectores de la vida nacional principalmente  en el sector   rural. Es un organismo autónomo que define sus propias políticas y acciones.  Surge de facto en 1999  a iniciativa de un  grupo de mujeres rurales  que acuden en busca de solidaridad y apoyo técnico  a un grupo de mujeres profesionales,  desde ese entonces se ha venido redefiniendo en la búsqueda de su identidad a través de las diversas etapas de su desarrollo, afianzando su actividad a partir de la diversidad, es decir, aceptando las diferencias culturales, jurídicas, económicas, sociales, educativas y políticas de las mujeres, para responder a los intereses tanto de género como globales.\r\nLa Fundación de Mujeres Rurales centró sus esfuerzos a lo largo del año de 1999 y parte de 2000 en la elaboración de una estrategia, la conceptualización de  Programas y Proyectos, con cuatro líneas básicas transversales: Sensibilización Social y Divulgación con metodología participativa, Movilización y Participación Ciudadana, Coordinaciones Interinstitucionales, Sostenibilidad y Replicabilidad.\r\nLa Fundación de Mujeres Rurales, conforme a su escritura de constitución, cuenta con dos órganos de Dirección, La Asamblea General de Miembros, que es la máxima autoridad y cuyas decisiones son de carácter imperativo, con las limitaciones que la ley establece; y un Consejo Directivo, que tiene como responsabilidad  el desarrollo de las labores administrativas. Las promotoras se consideran como parte operativa en la ejecución de las diferentes tareas y proyectos. Así la Fundación Mujeres Rurales posee la capacidad organizativa y de gestión para el desarrollo del proyecto desde la perspectiva comunal,  apoyándose en Casas de Familia existentes en las comunidades, asimismo cuenta con una cantidad muy importante de mujeres que actualmente se mueven alrededor de los diferentes programas, la gran mayoría de manera voluntaria.\r\n','2532-1230',''),(17,1,'Centro Ecuménico “ Fray Antonio de Valdivieso “','C.A.V','Casa Ricardo Morales Avilés, 6 C al sur Bo. Largaespada, Managua','1982-11-30','08','301182 - 9510 ','A – 15002-9','Marlon Stuart Almendarez ','ceav@turbonett.com','Enriqueta Ramírez de la Mota','2222-4577','','Formar y animar líderes populares capaces de promover la acción social y reanimar la esperanza en un mundo mejor.  Enfocamos nuestro trabajo hacia  los sectores populares, con especial énfasis en los jóvenes, mujeres, líderes rurales, líderes de barrios y dirigentes cristianos de base.','1.	Formación sobre violencia basada en Género y derechos sexuales y reproductivos, con un enfoque bíblico teológico, feminista.\r\n\r\n2.	Formación de liderazgo con un enfoque psicosocial.\r\n\r\n3.	Desarrollo rural y formación de liderazgo comunitario.','El CAV es fundado en 1979, con el propósito de “acompañar a los cristianos comprometidos con el proceso revolucionario”.\r\nDurante los años 80 se convirtió en la voz del movimiento de la Iglesia popular y en centro de difusión  de la teología de la liberación con proyección nacional e internacional en línea con su misión fundamental.  Complementaria impulso distintos proyectos de desarrollo.\r\nEn la década de los 90 el CAV mantuvo la actividad teológica e implementa nuevos programas y proyectos sociales: un programa de becas para estudiantes universitarios, acciones de apoyo de emergencia post Micth. Impulsa además, actividades políticas y de promoción de la acción ciudadana, etc.\r\nEl surgimiento de estos programas y actividades, sin embargo, no obedeció a un plan maestro o a una visión estratégica coherente y compartida por todos sus miembros. El CAV programas o proyectos que impulsaron sus actividades casi con total autonomía, con una diversidad de enfoques y planteamientos.\r\nActualmente, a partir de los aprendizajes generados por los procesos implementados, y los cambios en el contexto, el CAV se encuentra en una etapa de sistematización, divulgación y multiplicación de su quehacer; así como en un proceso de fortalecimiento institucional que implica la actualización de sus elementos estratégicos y la revisión y perfeccionamiento de aspectos administrativos, financieros y programáticos, a fin de mejorar la eficiencia y eficacia de su gestión.','2222-4577','2222-7955'),(18,1,'Asociación en Apoyo al Movimiento de NATRAS','Movimiento de NATRAS','Bo. San  Judas, ceibo 1c. arriba y 20 vrs al lago, Managua.','2000-07-07','1813','070700-9055','57881-5','Karla Sequeira Fletes','movimientodenatras@yahoo.es','Yamileth Ocampo Espinoza','8836-0525','','Contribuir a que NATRAS organizados y no organizados ocupen los espacios necesarios, propongan y demanden la defensa y el cumplimiento de sus derechos y deberes.','1) Monitoreo y seguimiento permanente: En las comunidades y municipios en que estemos presentes como Movimiento de NATRAS, haremos un seguimiento constante de la situación de los niños, niñas y adolescentes; del cumplimiento de sus derechos y del estado de las instituciones, políticas y servicios que deben garantizarlos; y del propio Movimiento de NATRAS, sus actividades y resultados.\r\n2) Incidencia y alianzas con otras organizaciones y sectores: distinguimos entre Incidencia local, como aquella incidencia en el entorno inmediato, en el que está la familia, los comerciantes, los maestros, en fin la comunidad; y la Incidencia nacional, también llamada incidencia política, por buscar incidir en lo político, en la toma de decisiones en los ámbitos de gobierno y administración, y en los espacios de participación. La incidencia tendrá como metas principales:\r\na.	Sensibilizar a distintos actores relevantes sobre la situación de NATRAS, para que no se nos explote y contribuyan a cumplir con nuestros derechos.\r\nb.	Facilitar la organización de nuestros grupos municipales.\r\nc.	Conseguir recursos económicos, tanto para apoyar el funcionamiento del Movimiento a nivel local y nacional, como para apoyar proyectos dirigidos a atender problemas y demandas de los NATRAS. Recaudación local y nacional de fondos, por diversos medios.\r\n3) Capacitación: la capacitación debe estar siempre incorporada en la planificación de todos nuestros procesos, para que todos los participantes de los mismos estén suficientemente informados, sensibilizados y motivados para asegurar la realización y cumplimiento de los objetivos que nos propongamos Se hará tanto con NATRAS como ex NATRAS, educadores, padres de familia y otros adultos, en temas concretos de nuestra situación y trabajo, utilizando herramientas y metodologías atractivas y nuevas. Debe ser permanente, para garantizar la renovación y la continuidad de nuestras acciones, estructuras y miembros.\r\n4) Participación a través de la Recreación: La recreación, un derecho y una necesidad para los niños, niñas y adolescentes en general, lo es aún más para los NATRAS, quienes por sus obligaciones laborales disponen de menos tiempo para ello y cargan con más tareas. Muchas organizaciones de adultos, al trabajar con niños, niñas y adolescentes, reproducen sus propios esquemas y formas de gestión formales y complicadas, que muchas veces limitan la inclusión de más NATRAS. El Movimiento de NATRAS, para responder mejor a los intereses, dinámicas, necesidades y aspiraciones de niños, niñas y adolescentes y cumplir al mismo tiempo con uno de sus derechos más básicos, adoptamos como estrategia desarrollar procesos, formas y métodos de participación, acción y capacitación que incorporen el juego y la recreación.\r\nNo descartamos espacios y mecanismos que requieren más formalidad en la discusión y elaboración de propuestas e incidencia; mas retomaremos estas dinámicas lúdicas para profundizarlos y hacerlos más efectivos e inclusivos, integrando a NATRAS actualmente excluidos.\r\n5) Sistematización y Transmisión de Experiencias: es importante sistematizar y transmitir las experiencias exitosas de niñas, niños y adolescentes trabajadores. Tanto como individuos, que muestran cómo por medio de su esfuerzo, entusiasmo y participación en el Movimiento mejoraron sus condiciones de vida y su desarrollo personal; como de su trayectoria en el Movimiento, que contienen los logros, las capacidades organizativas y conocimientos que adquirieron, y que les serán útiles a las siguientes generaciones integrantes del Movimiento de NATRAS.\r\n','El Movimiento de Niñas, Niños y Adolescentes Trabajadores (NATRAS) es una organización autónoma, sin fines de lucro, que existe desde 1991 conformada por los mismos chavalos y chavalas trabajadores en varios municipios y apoyados por diferentes ONG, que luchan por el cumplimiento integral de sus derechos, a través de su protagonismo y sus propios espacios de participación, así como el respeto y reconocimiento de la sociedad en general.\r\nSu propósito fundamental es estimular la propia organización de niñas, niños y adolescentes, para desarrollar alternativas que mejoren sus condiciones de vida y de trabajo, además de promover la transformación de las concepciones que ubican a la niñez como seres incapaces de reflexión y de actuación que provoquen cambios en su realidad. Por ello se promueven iniciativas que propongan el desarrollo de una niñez capaz de crear, criticar, reflexionar, comprender, aportar y transformar.\r\nSu visión es un Movimiento organizado y fortalecido con presencia local, nacional e internacional, que aglutina a NATRAS de todos los sectores, empoderada y reconocida, estando en promoción, defensa y goce de nuestros derechos y deberes.\r\nSu Misión es empoderar a niñas, niños y adolescentes trabajadores, organizándolos en espacios de participación y protagonismo propios con libre expresión y capacidad de decisión, para promover y defender sus derechos y cumplir sus deberes, dándoles mayores niveles de organización, sensibilización e incidencia y forjando alianzas con otros sectores sociales y organizaciones para mejorar el nivel de vida de niños, niñas y adolescentes y el cumplimiento pleno de sus derechos y deberes.\r\n','2260-0257',''),(19,1,'Unión de Cooperativas Agropecuarias “Augusto César Sandino” San Ramón','UCA San Ramón','Contiguo al Local donde fue la Policía Nacional San Ramón','1992-04-07','244','0410000020277','38773-8','Blanca Rosa Molina Torres ','gerencia@ucasanramon.com','Yadira Montenegro','2772-5247 ','','Fortalecer    capacidades en las cooperativas asociadas, socios, socias y sus familias que faciliten la apropiación y desarrollo de su organización con equidad  y  participación efectiva.','Estrategia A: Fortalecimiento Institucional de la UCA.\r\nA.1.Consolidado el Desarrollo  Organizacional de la UCA.\r\nA.2.Fortalecida la Sinergia de la UCA.\r\nEstrategia B: Fortalecimiento del desarrollo integral  de las cooperativas.\r\nB.1. Implementado Programa de capacitación dirigido a las cooperativas de base.\r\nB.2.  Ampliado el programa de Agroecoturismo Rural Comunitario a la mayoría de las cooperativas  de base.\r\nB.3. Ejecutados programas de infraestructura social de mejoramiento de condiciones de vida de los afiliados.\r\nB.4. Ejecutado un programa de asistencia integral dirigida a mejorar la condición y posición de las mujeres cooperativistas que incluya las acciones de la estrategia de equidad de género. \r\nB.5. Desarrollada la participación de las y los jóvenes en las cooperativas, generando capacidades orientadas a mejorar su  condición y posición. \r\n\r\nEstrategia C: Modernización Tecnológica para mejorar la competitividad.\r\nC.1.Agricultura sostenible, competitiva y fomento a la ganadería de doble propósito.\r\nC.2.Integración productiva de la familia en función de la protección del Ambiente.\r\nEstrategia D: Perfeccionamiento de la Gestión Financiera y Crediticia.\r\nD.1. Mejorado  el sistema de administración de cartera\r\nD.2. Impulsado programa de Gestión de fondos para financiamientos \r\n','Fue durante la década  de 1979-1989 con el gobierno Sandinista que se impulsa en Nicaragua, el proceso  de reforma agraria con el  objetivo fundamental  de entregar tierras a campesinos y campesinas  que no la poseían, en ese período fueron entregadas en carácter de cooperativas un total del 13% de las áreas del país, en el municipio de San Ramón se entregaron más de 8,000 hectáreas al sector cooperativo. \r\nAnte esa situación las cooperativas como agentes económicos importantes, readecuan su accionar individual y se organizan en bloques, de tal forma que les permitiera mayor poder organizativo, defensa de sus derechos, gestión, comercialización y producción, es decir enfrentar las adversidades de manera conjunta.\r\nEn la actualidad (2009)la UCA aglutina a 21 cooperativas atendiéndose de manera directa a  1,080,  socios: 388 mujeres (36%) y 692 hombres (75%), de una población alrededor de 6000 personas que representa el 40% del sector rural del municipio de San Ramón. \r\nTiene su área de influencia en el Municipio de san Ramón, y la distribución geográfica esta en las siguientes comarcas:\r\nYasica Sur, Sabana Grande,  Siare, Yucul, La Reina y sus comunidades (Monte  grande, El naranjo, Caserío La Reina), San Pablo, El Horno, Pueblo Viejo, Ocalca.\r\n','2772-5247 ',''),(20,1,'Fundación Puntos de Encuentro, para la transformación de la vida cotidiana ','Puntos de Encuentro ','Reparto Bolonia, Rotonda El Güegüense, 4 c. abajo 1 c. al lago, Managua, Nicaragua','1990-03-19','116','190390-9737','29075-9','Irela Solórzano Prado ','puntos@puntos.org.ni','Martha Juárez Ponce','2268-1227','','Somos una organizacion feminista y sin fines de lucro; que trabajamos para promover y fortalecer la defensa de los derechos de las mujeres y la accion colectiva del movimiento amplio de mujeres, y para fomentar un entorno social más favorable para que las mujeres jovenes y adultas tengan mayor capacidad y posibilidad de tomar control sobre sus propios cuerpos y participar en la toma de decisiones en los multiples ambitos que afectan sus vidas cotidianas. ','Nuestras estrategias vinculan la creación de medios masivos, capacitación con líderes de organizaciones y comunicadoras/es jóvenes, investigación aplicada y participación en redes e instancias de coordinación. \r\nPuntos parte de la convicción que lo personal es político y viceversa, y que la opresión, discriminación y violencia hacia las mujeres de todas las edades y condiciones sociales, son expresiones de relaciones desiguales de poder que se manifiestan desde lo más íntimo a lo más público. Por lo tanto, todas las acciones combinan aspectos vivenciales con análisis crítico, para llevar a la acción individual y colectiva. \r\n','Puntos de Encuentro es un referente internacional en el tema de comunicación para el cambio social, con años de experiencia en radio, producción audiovisual y comunicación escrita. Se ha comprobado su capacidad técnica y temática y de producción de series de televisión de enfoque social con gran alcance e impacto, en el contexto de una muy incipiente industria televisiva en Nicaragua. Cuenta con experticia en el campo del fortalecimiento de capacidades, diseño de metodologías y herramientas de trabajo con jóvenes, varios de los paquetes educativos, han sido adoptadas por varias organizaciones en Centroamérica, Bolivia y República Dominicana.','2268-1227',''),(21,1,'FUNDACION NIMEHUATZIN','NIMEHUATZIN','Repto. San Juan #611, Managua','1990-03-21','198','210390-9735','28743-3','Rita Arauz ','nimehuatzin@nimehuatzin.org','Johanna Ostrander','2278-0028','','Contribuir al Desarrollo Humano Sostenible a través de la prevención del VIH y SIDA, promoviendo el empoderamiento de las personas, con enfoque ético, de género y Derechos Humanos.','•	Investigación\r\n•	Incidencia en la formulación y aplicación de políticas públicas.\r\n•	Formación, Educación, Capacitación\r\n•	Comunicación masiva\r\n•	Atención Bio-psicosocial del VIH y el SIDA y ayuda humanitaria.\r\n','En veintiún años de trabajo, ha desarrollado una amplia y sólida experiencia en el abordaje de la epidemia del VIH desde una perspectiva amplia con participación de instituciones públicas y organizaciones privadas. Sus estrategias y actividades van orientadas a los agentes generadores de opinión y de cambio, tomadores de decisiones y quienes formulan las políticas públicas, operadores jurídicos, a las instituciones y activistas de derechos humanos, organizaciones de mujeres, voluntarias y voluntarios de diversos organismos, periodistas, religiosas, maestras, profesoras y profesores, personal de salud.','2278-0028','');
/*!40000 ALTER TABLE `fed_organizacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fed_poblacionmetadirecta`
--

DROP TABLE IF EXISTS `fed_poblacionmetadirecta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fed_poblacionmetadirecta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `proyecto_id` int(11) NOT NULL,
  `grupo_etareo` int(11) NOT NULL,
  `hombres` int(11) NOT NULL,
  `mujeres` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fed_poblacionmetadirecta_cf4ad9cb` (`proyecto_id`)
) ENGINE=MyISAM AUTO_INCREMENT=43 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fed_poblacionmetadirecta`
--

LOCK TABLES `fed_poblacionmetadirecta` WRITE;
/*!40000 ALTER TABLE `fed_poblacionmetadirecta` DISABLE KEYS */;
INSERT INTO `fed_poblacionmetadirecta` VALUES (1,3,1,0,19),(2,3,2,0,73),(3,3,3,0,472),(4,4,2,2779,25439),(5,4,3,1389,12719),(6,4,4,9726,89036),(7,7,3,0,601),(8,8,2,0,9),(9,8,3,5,69),(10,8,4,21,227),(11,10,1,20,22),(12,10,2,18,24),(13,10,4,23,48),(14,12,2,748,842),(15,13,2,400,1002),(16,13,3,0,2074),(17,13,4,0,5230),(18,14,3,50,50),(19,14,4,35,160),(20,15,4,0,5750),(21,16,3,783,1488),(22,16,4,1088,2071),(23,17,4,260,1400),(24,18,4,0,375),(25,19,2,81,111),(26,19,3,4,9),(27,19,4,114,234),(28,20,2,55,86),(29,20,3,91,80),(30,20,4,280,422),(31,21,1,90,90),(32,21,2,200,200),(33,21,3,300,300),(34,21,4,80,80),(35,23,1,115,80),(36,23,2,540,265),(37,23,3,700,345),(38,23,4,617,177),(39,24,1,14,15),(40,24,2,4,3),(41,24,3,65,60),(42,24,4,77,62);
/*!40000 ALTER TABLE `fed_poblacionmetadirecta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fed_poblacionmetaindirecta`
--

DROP TABLE IF EXISTS `fed_poblacionmetaindirecta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fed_poblacionmetaindirecta` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `proyecto_id` int(11) NOT NULL,
  `grupo_etareo` int(11) NOT NULL,
  `hombres` int(11) NOT NULL,
  `mujeres` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fed_poblacionmetaindirecta_cf4ad9cb` (`proyecto_id`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fed_poblacionmetaindirecta`
--

LOCK TABLES `fed_poblacionmetaindirecta` WRITE;
/*!40000 ALTER TABLE `fed_poblacionmetaindirecta` DISABLE KEYS */;
INSERT INTO `fed_poblacionmetaindirecta` VALUES (1,3,1,163,368),(2,3,2,135,536),(3,3,3,500,2950),(4,10,1,49,52),(5,10,2,54,48),(6,12,2,2572,3552),(7,13,2,697,356),(8,13,3,1440,7160),(9,13,4,161,9702),(10,14,3,577,738),(11,14,4,500,1560),(12,19,2,744,777),(13,19,4,103,213),(14,20,2,600,400),(15,20,3,500,700),(16,20,4,1500,2300),(17,21,2,40,40),(18,21,3,80,80),(19,21,4,80,80),(20,24,2,1350,7650),(21,24,3,12250,12750),(22,24,4,4900,5100);
/*!40000 ALTER TABLE `fed_poblacionmetaindirecta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fed_proyecto`
--

DROP TABLE IF EXISTS `fed_proyecto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fed_proyecto` (
  `organizacion_id` int(11) NOT NULL,
  `codigo` varchar(100) NOT NULL,
  `nombre` longtext NOT NULL,
  `modalidad` int(11) NOT NULL,
  `cobertura` int(11) NOT NULL,
  `fecha_inicio` date NOT NULL DEFAULT '2011-06-08',
  `fecha_fin` date NOT NULL DEFAULT '2011-06-08',
  `monto_fed` decimal(30,2),
  `monto_contrapartida` decimal(30,2),
  `monto_otros` decimal(30,2),
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `codigo` (`codigo`),
  KEY `fed_proyecto_48753264` (`organizacion_id`)
) ENGINE=MyISAM AUTO_INCREMENT=25 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fed_proyecto`
--

LOCK TABLES `fed_proyecto` WRITE;
/*!40000 ALTER TABLE `fed_proyecto` DISABLE KEYS */;
INSERT INTO `fed_proyecto` VALUES (3,'FED-AP-01-2010','Plan Estratégico 2010-2012',1,3,'2010-06-01','2012-05-31','500000.00','266293.68','656868.44',4),(2,'FED-CP- 099-2010','Apoyo Institucional para el trabajo de Prevención y Atención de la Violencia Intrafamiliar y Sexual.',2,1,'2010-04-01','2011-03-31','33000.00','16500.00','0.00',3),(4,'FED-AP-04-2010','Propuesta de Apoyo Programático',1,3,'2010-10-15','2012-10-15','250000.00','74159.00','1123774.00',7),(5,'FED-016-2010','Contribución al desarrollo de capacidades sobre el Derecho a la Integridad: Sexualidad Libre de Violencia en un marco de relaciones de equidad, respeto y justicia y el Derecho a la SSR y sus riesgos (Embarazos en la Adolescencia, ITS.-VIH en la población del Departamento de León.',2,2,'2010-04-01','2011-03-31','103000.00','31186.00','19750.00',8),(6,'FED-032-2010','Construcción de alianzas para el empoderamiento de las mujeres y la creación de observatorios de violencia y embarazos tempranos en cuatro comunidades del departamento de Managua.',2,2,'2010-04-01','2012-04-30','236000.00','60596.00','0.00',9),(7,'FED-076-2010','Participación de niñas, niños, adolescentes y jóvenes en la promoción de sus derechos sexuales, derechos reproductivos y vivir sin violencia. ',2,2,'2010-04-01','2011-03-31','82200.00','40863.00','80000.00',10),(9,'FED – 070- 2010','“Empoderando a mujeres organizadas del departamento de Masaya para el ejercicio de sus derechos sexuales y derechos reproductivos en el ámbito de la prevención”',2,2,'2010-04-01','2011-03-31','90100.00','8397.00','18318.00',11),(11,'FED 074 - 2010','Estrategia comunicacional participativa para la promoción del Derecho a una información adecuada y oportuna de la salud sexual y reproductiva.',2,2,'2010-04-01','2012-03-31','69100.00','50373.00','0.00',12),(12,'FED-081-2010','Mujeres del Norte de Nicaragua por la igualdad en el país y en la casa.',2,2,'2010-04-01','2012-03-31','293200.00','14040.00','67616.00',13),(13,'FED-066-2010','Desarrollando capacidades para reducir el riesgo de violencia basada en género.',2,1,'2010-04-01','2012-03-31','93300.00','0.00','53000.00',14),(14,'FED- 057-2010','Fortalecimiento de la Ciudadanía de las Mujeres nicaragüenses para la defensa de los derechos sexuales y reproductivos.',2,3,'2010-04-01','2011-07-31','193000.00','33896.00','0.00',15),(15,'FED-027-2010','Por una Agenda de los Derechos Humanos con Perspectiva de Género',2,1,'2010-04-01','2011-03-31','52300.00','16200.00','39831.00',16),(16,'FED – 122 -2010','Desarrollo de capacidad local para la promoción de la salud sexual y reproductiva a nivel comunitario.',2,2,'2010-04-01','2012-03-31','127800.00','18343.00','0.00',17),(17,'FED- 087-2010','Proceso formativo sobre Derechos Sexuales  y Reproductivos con Enfoque Teológico.',2,2,'2010-04-01','2011-03-31','46500.00','4200.00','0.00',18),(18,'FED 133-2010','Mi derecho a vivir sin violencia.',2,2,'2010-04-01','2011-03-31','50000.00','4120.00','7435.00',19),(19,'FED-061-2010','Empoderándonos de nuestros derechos e incidiendo en nuestras cooperativas y en el ámbito público.',2,1,'2010-04-01','2012-03-31','138000.00','17524.00','0.00',20),(8,'FED-120-2010','Promoviendo el derecho  de las personas con Discapacidad a vivir en una ambiente libre de violencia. 1ra fase',2,3,'2010-04-01','2011-03-31','70000.00','0.00','18522.00',21),(20,'FED-AP-02-2010','Plan Estratégico 2010-2012. ',1,3,'2010-06-01','2012-05-30','400000.00','28600.00','1558746.00',22),(10,'FED-007-2010','Mujeres y jóvenes protagonistas de su empoderamiento',2,2,'2010-04-01','2012-03-31','234500.00','25996.00','73368.00',23),(21,'FED-AP-03-2010','Plan Estrategico de Nimehuatzin',1,3,'2010-10-15','2011-10-15','75000.00','0.00','0.00',24);
/*!40000 ALTER TABLE `fed_proyecto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fed_proyecto_otros_donantes`
--

DROP TABLE IF EXISTS `fed_proyecto_otros_donantes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fed_proyecto_otros_donantes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `proyecto_id` int(11) NOT NULL,
  `donante_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fed_proyecto_otros_donantes_proyecto_id_3725a3157631795a_uniq` (`proyecto_id`,`donante_id`),
  KEY `fed_proyecto_otros_donantes_cf4ad9cb` (`proyecto_id`),
  KEY `fed_proyecto_otros_donantes_743f2de0` (`donante_id`)
) ENGINE=MyISAM AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fed_proyecto_otros_donantes`
--

LOCK TABLES `fed_proyecto_otros_donantes` WRITE;
/*!40000 ALTER TABLE `fed_proyecto_otros_donantes` DISABLE KEYS */;
INSERT INTO `fed_proyecto_otros_donantes` VALUES (1,11,1),(2,11,2),(3,11,3),(4,13,4),(5,13,5),(6,13,6),(7,13,7),(8,13,8),(9,13,9),(10,13,10),(11,14,11),(12,14,12),(13,16,13),(14,19,14),(15,21,16),(16,21,17),(17,21,18),(18,21,15),(19,22,19),(20,22,20),(21,22,21),(22,22,22),(23,22,23),(24,22,24),(25,22,25),(26,22,26),(27,22,27),(28,22,28),(29,23,29);
/*!40000 ALTER TABLE `fed_proyecto_otros_donantes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fed_proyecto_resultados`
--

DROP TABLE IF EXISTS `fed_proyecto_resultados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fed_proyecto_resultados` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `proyecto_id` int(11) NOT NULL,
  `resultado_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fed_proyecto_resultados_proyecto_id_30a87ecac957297a_uniq` (`proyecto_id`,`resultado_id`),
  KEY `fed_proyecto_resultados_cf4ad9cb` (`proyecto_id`),
  KEY `fed_proyecto_resultados_f19cccaa` (`resultado_id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fed_proyecto_resultados`
--

LOCK TABLES `fed_proyecto_resultados` WRITE;
/*!40000 ALTER TABLE `fed_proyecto_resultados` DISABLE KEYS */;
INSERT INTO `fed_proyecto_resultados` VALUES (5,3,5),(4,3,4),(6,4,1),(7,4,2),(8,4,3),(9,4,4),(10,4,5),(11,7,1),(12,7,2),(13,7,3),(14,7,4),(15,7,5),(29,8,3),(20,10,4),(19,10,3),(21,11,1),(22,11,2),(23,11,3),(24,11,4),(25,11,5),(26,12,2),(27,12,3),(28,12,4),(30,13,1),(31,13,2),(32,13,3),(33,13,4),(34,13,5),(35,14,4),(36,15,2),(37,15,3),(38,16,4),(39,16,5),(40,17,3),(41,17,4),(42,17,5),(43,18,3),(44,18,4),(45,19,4),(46,20,3),(47,20,4),(48,20,5),(49,21,4),(50,21,5),(51,22,1),(52,22,2),(53,22,3),(54,22,4),(55,22,5),(56,23,3),(57,23,4),(58,23,5),(59,24,2),(60,24,3);
/*!40000 ALTER TABLE `fed_proyecto_resultados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fed_resultado`
--

DROP TABLE IF EXISTS `fed_resultado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fed_resultado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_corto` varchar(35) NOT NULL,
  `descripcion` longtext NOT NULL,
  `codigo` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fed_resultado`
--

LOCK TABLES `fed_resultado` WRITE;
/*!40000 ALTER TABLE `fed_resultado` DISABLE KEYS */;
INSERT INTO `fed_resultado` VALUES (1,'Resultado 1.1','Descripcion del Resultado numero uno',1),(2,'Resultado 1.2','Descripcion del resultado numero 2',2),(3,'Resultado 2.1','OSC logran el involucramiento de las poblaciones metas en procesos de reflexión sobre los derechos sexuales y derechos reproductivos dirigidos a una sexualidad integral, placentera, responsable, segura y libre de prejuicios',3),(4,'Resultado 2.2','Fortalecida la prevención de la violencia basada en género',4),(5,'Resultado 2.3','Acceso a servicios de atención integral y demanda de salud y justicia para las victimas de violencia de genero.\r\n',5),(6,'Resultado 3.1','Fortalecida la capacidad técnica de las OSC contrapartes del FED.\r\n',6);
/*!40000 ALTER TABLE `fed_resultado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fed_tema`
--

DROP TABLE IF EXISTS `fed_tema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fed_tema` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fed_tema`
--

LOCK TABLES `fed_tema` WRITE;
/*!40000 ALTER TABLE `fed_tema` DISABLE KEYS */;
INSERT INTO `fed_tema` VALUES (1,'Prevención de la violencia de género'),(2,'Salud Sexual y Reproductiva'),(3,'Atención en salud a víctimas de violencia'),(4,'VIH y SIDA'),(5,'Masculinidad'),(6,'Diversidad sexual'),(7,'Aborto terapeutico');
/*!40000 ALTER TABLE `fed_tema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fed_tematrabajo`
--

DROP TABLE IF EXISTS `fed_tematrabajo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fed_tematrabajo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `proyecto_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fed_tematrabajo_cf4ad9cb` (`proyecto_id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fed_tematrabajo`
--

LOCK TABLES `fed_tematrabajo` WRITE;
/*!40000 ALTER TABLE `fed_tematrabajo` DISABLE KEYS */;
INSERT INTO `fed_tematrabajo` VALUES (1,3),(2,4),(3,7),(4,8),(5,9),(6,10),(7,11),(8,12),(9,13),(10,14),(11,15),(12,16),(13,17),(14,18),(15,19),(16,20),(17,21),(18,22),(19,23),(20,24);
/*!40000 ALTER TABLE `fed_tematrabajo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fed_tematrabajo_municipio`
--

DROP TABLE IF EXISTS `fed_tematrabajo_municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fed_tematrabajo_municipio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tematrabajo_id` int(11) NOT NULL,
  `municipio_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fed_tematrabajo_municipio_tematrabajo_id_20adcd20c94ea1fa_uniq` (`tematrabajo_id`,`municipio_id`),
  KEY `fed_tematrabajo_municipio_f44fafa7` (`tematrabajo_id`),
  KEY `fed_tematrabajo_municipio_f3143aaa` (`municipio_id`)
) ENGINE=MyISAM AUTO_INCREMENT=425 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fed_tematrabajo_municipio`
--

LOCK TABLES `fed_tematrabajo_municipio` WRITE;
/*!40000 ALTER TABLE `fed_tematrabajo_municipio` DISABLE KEYS */;
INSERT INTO `fed_tematrabajo_municipio` VALUES (1,1,6510),(2,2,545),(3,2,3045),(4,2,7015),(5,2,8040),(6,2,1035),(7,2,6510),(8,2,5010),(9,2,2515),(10,2,3540),(11,2,5525),(12,2,7510),(13,2,9110),(14,2,6010),(15,2,9340),(16,2,4030),(17,3,545),(18,3,4005),(19,3,3055),(20,3,2515),(21,3,3540),(22,3,5525),(23,3,2010),(24,3,4015),(25,3,2005),(26,4,3520),(27,4,3525),(28,4,3530),(29,4,3535),(30,4,3505),(31,4,3540),(32,4,3510),(33,4,3545),(34,4,3515),(35,4,3550),(36,5,5522),(37,5,5515),(38,5,5525),(39,6,4035),(40,6,4030),(41,7,6025),(42,7,6010),(43,7,6005),(44,7,6030),(45,7,6015),(46,8,2505),(47,8,2530),(48,8,2515),(49,8,2525),(50,8,2510),(51,9,4065),(52,9,4035),(53,9,1010),(54,9,4040),(55,9,4010),(56,9,1035),(57,9,4045),(58,9,4015),(59,9,9105),(60,9,4050),(61,9,4055),(62,9,9305),(63,9,4030),(64,10,5525),(65,11,3030),(66,11,6025),(67,11,6030),(68,11,9105),(69,11,530),(70,11,5525),(71,11,9110),(72,11,9115),(73,11,9120),(74,11,9130),(75,11,4030),(76,11,2505),(77,11,2510),(78,11,3025),(79,11,4050),(80,11,2515),(81,11,3540),(82,11,7510),(83,11,2520),(84,11,4060),(85,11,9315),(86,11,3045),(87,11,6005),(88,11,9335),(89,11,6010),(90,11,9340),(91,11,6015),(92,12,9110),(93,13,7520),(94,13,7540),(95,13,7510),(96,14,5505),(97,14,2515),(98,14,3540),(99,14,5525),(100,15,7520),(101,15,7015),(102,15,4015),(103,15,7505),(104,15,3540),(105,15,4030),(106,16,4035),(107,16,4030),(108,17,1025),(109,17,515),(110,17,1030),(111,17,520),(112,17,1035),(113,17,525),(114,17,1040),(115,17,530),(116,17,535),(117,17,4015),(118,17,540),(119,17,545),(120,17,550),(121,17,555),(122,17,560),(123,17,9305),(124,17,9310),(125,17,9312),(126,17,9315),(127,17,9316),(128,17,9320),(129,17,7015),(130,17,9325),(131,17,9330),(132,17,4030),(133,17,9335),(134,17,9340),(135,17,9345),(136,17,9323),(137,17,1012),(138,17,3065),(139,17,8505),(140,17,2015),(141,17,8510),(142,17,8515),(143,17,8005),(144,17,8520),(145,17,8010),(146,17,8525),(147,17,8015),(148,17,7505),(149,17,8530),(150,17,8020),(151,17,7510),(152,17,8025),(153,17,7515),(154,17,7005),(155,17,8030),(156,17,7520),(157,17,7010),(158,17,8035),(159,17,7525),(160,17,6545),(161,17,8040),(162,17,6505),(163,17,7530),(164,17,6507),(165,17,7020),(166,17,8045),(167,17,6510),(168,17,7535),(169,17,8050),(170,17,6515),(171,17,7540),(172,17,6005),(173,17,6520),(174,17,6010),(175,17,6525),(176,17,6015),(177,17,5505),(178,17,6530),(179,17,6020),(180,17,5510),(181,17,6535),(182,17,6025),(183,17,5515),(184,17,6540),(185,17,5005),(186,17,6030),(187,17,5520),(188,17,9105),(189,17,5522),(190,17,6035),(191,17,5525),(192,17,9110),(193,17,5015),(194,17,6040),(195,17,5530),(196,17,9115),(197,17,5020),(198,17,6045),(199,17,5535),(200,17,9120),(201,17,5025),(202,17,9125),(203,17,5030),(204,17,9127),(205,17,5532),(206,17,9130),(207,17,9135),(208,17,3505),(209,17,4020),(210,17,3510),(211,17,4025),(212,17,3515),(213,17,3005),(214,17,5010),(215,17,3520),(216,17,3010),(217,17,4035),(218,17,3525),(219,17,3015),(220,17,4040),(221,17,2505),(222,17,3530),(223,17,3020),(224,17,4045),(225,17,2510),(226,17,3535),(227,17,3025),(228,17,4050),(229,17,2515),(230,17,3540),(231,17,2005),(232,17,3030),(233,17,4055),(234,17,2520),(235,17,3545),(236,17,2010),(237,17,3035),(238,17,4060),(239,17,2525),(240,17,3550),(241,17,4005),(242,17,3040),(243,17,4065),(244,17,2530),(245,17,2020),(246,17,3045),(247,17,2025),(248,17,3050),(249,17,2045),(250,17,1005),(251,17,2030),(252,17,3055),(253,17,1010),(254,17,2035),(255,17,3060),(256,17,1015),(257,17,2040),(258,17,505),(259,17,1020),(260,17,4010),(261,17,510),(262,18,1025),(263,18,515),(264,18,1030),(265,18,520),(266,18,1035),(267,18,525),(268,18,1040),(269,18,530),(270,18,535),(271,18,4015),(272,18,540),(273,18,545),(274,18,550),(275,18,555),(276,18,560),(277,18,9305),(278,18,9310),(279,18,9312),(280,18,9315),(281,18,9316),(282,18,9320),(283,18,7015),(284,18,9325),(285,18,9330),(286,18,4030),(287,18,9335),(288,18,9340),(289,18,9345),(290,18,9323),(291,18,1012),(292,18,3065),(293,18,8505),(294,18,2015),(295,18,8510),(296,18,8515),(297,18,8005),(298,18,8520),(299,18,8010),(300,18,8525),(301,18,8015),(302,18,7505),(303,18,8530),(304,18,8020),(305,18,7510),(306,18,8025),(307,18,7515),(308,18,7005),(309,18,8030),(310,18,7520),(311,18,7010),(312,18,8035),(313,18,7525),(314,18,6545),(315,18,8040),(316,18,6505),(317,18,7530),(318,18,6507),(319,18,7020),(320,18,8045),(321,18,6510),(322,18,7535),(323,18,8050),(324,18,6515),(325,18,7540),(326,18,6005),(327,18,6520),(328,18,6010),(329,18,6525),(330,18,6015),(331,18,5505),(332,18,6530),(333,18,6020),(334,18,5510),(335,18,6535),(336,18,6025),(337,18,5515),(338,18,6540),(339,18,5005),(340,18,6030),(341,18,5520),(342,18,9105),(343,18,5522),(344,18,6035),(345,18,5525),(346,18,9110),(347,18,5015),(348,18,6040),(349,18,5530),(350,18,9115),(351,18,5020),(352,18,6045),(353,18,5535),(354,18,9120),(355,18,5025),(356,18,9125),(357,18,5030),(358,18,9127),(359,18,5532),(360,18,9130),(361,18,9135),(362,18,3505),(363,18,4020),(364,18,3510),(365,18,4025),(366,18,3515),(367,18,3005),(368,18,5010),(369,18,3520),(370,18,3010),(371,18,4035),(372,18,3525),(373,18,3015),(374,18,4040),(375,18,2505),(376,18,3530),(377,18,3020),(378,18,4045),(379,18,2510),(380,18,3535),(381,18,3025),(382,18,4050),(383,18,2515),(384,18,3540),(385,18,2005),(386,18,3030),(387,18,4055),(388,18,2520),(389,18,3545),(390,18,2010),(391,18,3035),(392,18,4060),(393,18,2525),(394,18,3550),(395,18,4005),(396,18,3040),(397,18,4065),(398,18,2530),(399,18,2020),(400,18,3045),(401,18,2025),(402,18,3050),(403,18,2045),(404,18,1005),(405,18,2030),(406,18,3055),(407,18,1010),(408,18,2035),(409,18,3060),(410,18,1015),(411,18,2040),(412,18,505),(413,18,1020),(414,18,4010),(415,18,510),(416,19,520),(417,19,505),(418,19,515),(419,19,510),(420,19,555),(421,20,8040),(422,20,6010),(423,20,5525),(424,20,7510);
/*!40000 ALTER TABLE `fed_tematrabajo_municipio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fed_tematrabajo_tema`
--

DROP TABLE IF EXISTS `fed_tematrabajo_tema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fed_tematrabajo_tema` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tematrabajo_id` int(11) NOT NULL,
  `tema_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `fed_tematrabajo_tema_tematrabajo_id_2aed60ddaef74776_uniq` (`tematrabajo_id`,`tema_id`),
  KEY `fed_tematrabajo_tema_f44fafa7` (`tematrabajo_id`),
  KEY `fed_tematrabajo_tema_e189947` (`tema_id`)
) ENGINE=MyISAM AUTO_INCREMENT=61 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fed_tematrabajo_tema`
--

LOCK TABLES `fed_tematrabajo_tema` WRITE;
/*!40000 ALTER TABLE `fed_tematrabajo_tema` DISABLE KEYS */;
INSERT INTO `fed_tematrabajo_tema` VALUES (1,1,1),(2,2,1),(3,2,2),(4,2,3),(5,2,4),(6,2,5),(7,2,6),(8,2,7),(9,3,1),(10,3,2),(11,3,3),(12,3,4),(13,3,5),(14,3,6),(15,4,1),(16,4,2),(17,4,3),(18,4,4),(19,5,1),(20,6,1),(21,6,2),(22,6,5),(23,7,1),(24,7,2),(25,7,3),(26,7,4),(27,8,2),(28,8,4),(29,8,5),(30,8,6),(31,9,1),(32,9,2),(33,9,3),(34,9,6),(35,9,7),(36,10,1),(37,10,5),(38,11,2),(39,11,6),(40,11,7),(41,12,1),(42,12,3),(43,13,2),(44,14,1),(45,15,1),(46,16,1),(47,16,2),(48,16,3),(49,16,4),(50,16,5),(51,17,1),(52,17,3),(53,18,1),(54,18,2),(55,19,1),(56,19,2),(57,19,3),(58,19,4),(59,19,7),(60,20,4);
/*!40000 ALTER TABLE `fed_tematrabajo_tema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_departamento`
--

DROP TABLE IF EXISTS `lugar_departamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_departamento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `extension` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_departamento`
--

LOCK TABLES `lugar_departamento` WRITE;
/*!40000 ALTER TABLE `lugar_departamento` DISABLE KEYS */;
INSERT INTO `lugar_departamento` VALUES (5,'Nueva Segovia','Nueva-segovia','3491.28'),(10,'Jinotega','jinotega','9222.40'),(20,'Madriz','madriz','1708.23'),(25,'Estelí','esteli','2229.69'),(30,'Chinandega','chinandega','4822.46'),(35,'León','leon','5138.03'),(40,'Matagalpa','matagalpa','6803.86'),(50,'Boaco','boaco','4176.68'),(55,'Managua','managua','3465.10'),(60,'Masaya','masaya','610.78'),(65,'Chontales','chontales','6481.27'),(70,'Granada','granada','1039.68'),(75,'Carazo','carazo','1081.40'),(80,'Rivas','rivas','2161.82'),(85,'Rí­o San Juan','Rio-san-juan','7540.90'),(91,'RAAN','RAAN','32819.68'),(93,'RAAS','RAAS','27546.32'),(99,'Cobertura Nacional','cobertura-nacional','333333.00');
/*!40000 ALTER TABLE `lugar_departamento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lugar_municipio`
--

DROP TABLE IF EXISTS `lugar_municipio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lugar_municipio` (
  `id` int(11) NOT NULL,
  `departamento_id` int(11) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `slug` varchar(50) DEFAULT NULL,
  `extension` decimal(10,2) DEFAULT NULL,
  `latitud` decimal(8,5) DEFAULT NULL,
  `longitud` decimal(8,5) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`),
  UNIQUE KEY `slug` (`slug`),
  KEY `lugar_municipio_8865b15a` (`departamento_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lugar_municipio`
--

LOCK TABLES `lugar_municipio` WRITE;
/*!40000 ALTER TABLE `lugar_municipio` DISABLE KEYS */;
INSERT INTO `lugar_municipio` VALUES (505,5,'Jalapa','jalapa','0.00','13.92286','-86.12520'),(510,5,'Murra','murra','0.00','13.75900','-86.01799'),(515,5,'El Jí­caro','El-jicaro','0.00','13.72326','-86.13705'),(520,5,'San Fernando','San-fernando','0.00','13.67729','-86.31484'),(525,5,'Mozonte','mozonte','0.00','13.66168','-86.43706'),(530,5,'Dipilto','dipilto','0.00','13.72243','-86.50720'),(535,5,'Macuelizo','macuelizo','0.00','13.65239','-86.61380'),(540,5,'Santa Marí­a','santamaria','0.00','13.74753','-86.71077'),(545,5,'Ocotal','ocotal','0.00','13.63432','-86.47745'),(550,5,'Ciudad Antigua','Ciudad-antigua','0.00','13.64217','-86.30893'),(555,5,'Quilalí','quilali','0.00','13.56675','-86.02952'),(560,5,'Wiwili de Nueva Segovia','Wiwili-nuevasegovia','0.00','13.62667','-85.82369'),(1005,10,'Wiwilí','Wiwili','0.00','13.62130','-85.81864'),(1010,10,'El Cúa','El-cua','0.00','13.36764','-85.67330'),(1012,10,'San José Bocay','San-jose-bocay','0.00','13.61976','-85.50080'),(1015,10,'Sta. María de Pantasma','Santa-maria-pantasma','0.00','13.36667','-85.95000'),(1020,10,'San Rafael del Norte','San-rafael-del-norte','0.00','13.21391','-86.11043'),(1025,10,'San Sebastian de Yalí','yali','0.00','13.30500','-86.18636'),(1030,10,'La Concordia','La-concordia','0.00','13.19535','-86.16693'),(1035,10,'Jinotega','jinotega','0.00','13.09165','-86.00121'),(2005,20,'Somoto','somoto','0.00','13.48129','-86.58337'),(2010,20,'Totogalpa','totogalpa','0.00','13.56336','-86.49281'),(2015,20,'Telpaneca','telpaneca','0.00','13.53131','-86.28693'),(2020,20,'San Juan de Río Coco','San-juan-rio-coco','0.00','13.54458','-86.16537'),(2025,20,'Palacaguina','palacaguina','0.00','13.45597','-86.40710'),(2030,20,'Yalaguina','yalaguina','0.00','13.48351','-86.49344'),(2035,20,'San Lucas','San-lucas','0.00','13.41358','-86.61176'),(2040,20,'Las Sabanas','Las-sabanas','0.00','13.34324','-86.62194'),(2045,20,'San José de Cusmapa','San-jose-cusmapa','0.00','13.28847','-86.65489'),(2505,25,'Pueblo Nuevo','Pueblo-nuevo','0.00','13.37937','-86.48077'),(2510,25,'Condega','condega','0.00','13.36213','-86.39789'),(2515,25,'Estelí','esteli','0.00','13.08948','-86.35551'),(2520,25,'San Juan de Limay','Sanjuan-limay','0.00','13.17489','-86.61234'),(2525,25,'La Trinidad','trinidad','0.00','12.96823','-86.23604'),(2530,25,'San Nicolás','San-nicolas','0.00','12.93312','-86.34700'),(3005,30,'San Pedro del Norte','San-pedro-del-norte','0.00','13.27596','-86.87777'),(3010,30,'San Francisco del Norte','San-francisco-del-norte','0.00','13.20016','-86.77192'),(3015,30,'Cinco Pinos','Cinco-pinos','0.00','13.23036','-86.86719'),(3020,30,'Santo Tomás del Norte','Santo-tomas-del-norte','0.00','13.18701','-86.92352'),(3025,30,'El Viejo','El-viejo','0.00','12.66228','-87.16541'),(3030,30,'Pto. Morazán','Puerto-morazan','0.00','12.76721','-87.13388'),(3035,30,'Somotillo','somotillo','0.00','13.04495','-86.90499'),(3040,30,'Villanueva','villanueva','0.00','12.96391','-86.81468'),(3045,30,'Chinandega','chinandega','0.00','12.62872','-87.13149'),(3050,30,'El Realejo','El-realejo','0.00','12.54551','-87.16736'),(3055,30,'Corinto','corinto','0.00','12.48461','-87.17122'),(3060,30,'Chichigalpa','chichigalpa','0.00','12.57224','-87.02849'),(3065,30,'Posoltega','posotelga','0.00','12.54410','-86.98010'),(3505,35,'Achuapa','achuapa','0.00','13.05433','-86.59070'),(3510,35,'El Sauce','El-sauce','0.00','12.88694','-86.53952'),(3515,35,'Santa Rosa del Peñon','Santa-rosa-del-penon','0.00','12.80142','-86.37144'),(3520,35,'El Jicaral','El-jicaral','0.00','12.72672','-86.38134'),(3525,35,'Larreynaga','larreynaga','0.00','12.59311','-86.68015'),(3530,35,'Telica','telica','0.00','12.52152','-86.86030'),(3535,35,'Quezalguaque','quezalguaque','0.00','12.50614','-86.90366'),(3540,35,'León','leon','0.00','12.43481','-86.88174'),(3545,35,'La Paz Centro','La-paz-centro','0.00','12.34011','-86.67625'),(3550,35,'Nagarote','nagarote','0.00','12.26531','-86.56812'),(4005,40,'Rancho Grande','Rancho-grande','0.00','13.25352','-85.55268'),(4010,40,'Rí­o Blanco','Rio-blanco','0.00','12.93044','-85.22610'),(4015,40,'El Tuma - La Dalia','El-tuma','0.00','13.13735','-85.73788'),(4020,40,'San Isidro','San-isidro','0.00','12.92937','-86.19550'),(4025,40,'Sébaco','sebaco','0.00','12.85190','-86.09696'),(4030,40,'Matagalpa','matagalpa','0.00','12.92709','-85.91747'),(4035,40,'San Ramón','San-ramon','0.00','12.92254','-85.83968'),(4040,40,'Matiguás','matiguas','0.00','12.83710','-85.46079'),(4045,40,'Muy Muy','muymuy','0.00','12.76125','-85.63123'),(4050,40,'Esquipulas','esquipulas','0.00','12.66446','-85.78909'),(4055,40,'San Dionisio','San-dionisio','0.00','12.76190','-85.85091'),(4060,40,'Terrabona','terrabona','0.00','12.73009','-85.96487'),(4065,40,'Ciudad Darí­o','Ciudad-dario','0.00','12.73000','-86.12457'),(5005,50,'San José de los Remates','San-jose-de-los-remates','0.00','12.59748','-85.76253'),(5010,50,'Boaco','boaco','0.00','12.47160','-85.65952'),(5015,50,'Camoapa','camoapa','0.00','12.38377','-85.51465'),(5020,50,'Santa Lucía','Santa-lucia','0.00','12.53226','-85.71156'),(5025,50,'Teustepe','teustepe','0.00','12.41979','-85.79922'),(5030,50,'San  Lorenzo','San-lorenzo','0.00','12.37789','-85.66718'),(5505,55,'San Francisco Libre','San-francisco-libre','0.00','12.50458','-86.30105'),(5510,55,'Tipitapa','tipitapa','0.00','12.19662','-86.09682'),(5515,55,'Mateare','mateare','0.00','12.23536','-86.43013'),(5520,55,'Villa Carlos Fonseca','Villa-carlos-fonseca','0.00','11.97924','-86.50809'),(5522,55,'Ciudad Sandino','Ciudad-sandino','0.00','12.16082','-86.35004'),(5525,55,'Managua','managua','0.00','12.14746','-86.27339'),(5530,55,'Ticuantepe','ticuantepe','0.00','12.02125','-86.20288'),(5532,55,'El Crucero','El-crucero','0.00','11.97865','-86.31076'),(5535,55,'San Rafael del Sur','San-rafael-del-sur','0.00','11.84681','-86.43977'),(6005,60,'Nindirí','nindiri','0.00','12.00243','-86.12067'),(6010,60,'Masaya','masaya','0.00','11.97735','-86.09606'),(6015,60,'Tisma','tisma','0.00','12.08133','-86.01921'),(6020,60,'La Concepción','La-concepcion','0.00','11.93615','-86.19220'),(6025,60,'Masatepe','masatepe','0.00','11.91344','-86.14475'),(6030,60,'Nandasmo','nandasmo','0.00','11.90933','-86.13055'),(6035,60,'Catarina','catarina','0.00','11.91078','-86.07407'),(6040,60,'San Juan de Oriente','San-juan-de-oriente','0.00','11.90479','-86.07311'),(6045,60,'Niquinohomo','niquinomo','0.00','11.90408','-86.09472'),(6505,65,'Comalapa','comalapa','0.00','12.28340','-85.51142'),(6507,65,'San Francisco Cuapa','San-francisco-cuapa','0.00','12.26671','-85.38308'),(6510,65,'Juigalpa','juigalpa','0.00','12.10580','-85.36842'),(6515,65,'La Libertad','La-libertad','0.00','12.21539','-85.16549'),(6520,65,'Santo Domingo','Santo-domingo','0.00','12.26301','-85.08232'),(6525,65,'Santo Tomás','Santo-tomas','0.00','12.06902','-85.09340'),(6530,65,'San Pedro de Lóvago','San-pedro-de-lovago','0.00','12.12852','-85.11572'),(6535,65,'Acoyapa','acoyapa','0.00','11.96764','-85.17044'),(6540,65,'Villa Sandino','Villa-sandino','0.00','12.04779','-84.99334'),(6545,65,'El Coral','El-coral','0.00','11.91576','-84.65041'),(7005,70,'Diriá','diria','0.00','11.88416','-86.05565'),(7010,70,'Diriomo','diriomo','0.00','11.87494','-86.05110'),(7015,70,'Granada','granada','0.00','11.93095','-85.95696'),(7020,70,'Nandaime','nandaime','0.00','11.75630','-86.05345'),(7505,75,'San Marcos','San-marcos','0.00','11.90651','-86.20314'),(7510,75,'Jinotepe','jinotepe','0.00','11.84831','-86.19846'),(7515,75,'Dolores','dolores','0.00','11.85565','-86.21535'),(7520,75,'Diriamba','diriamba','0.00','11.85572','-86.24074'),(7525,75,'El Rosario','El-rosario','0.00','11.83224','-86.16484'),(7530,75,'La Paz de Carazo','La-paz-de-carazo','0.00','11.82206','-86.12750'),(7535,75,'Santa Teresa','Santa-tereza','0.00','11.80272','-86.16281'),(7540,75,'La Conquista','La-conquista','0.00','11.73336','-86.19297'),(8005,80,'Tola','tola','0.00','11.43868','-85.93907'),(8010,80,'Belén','belen','0.00','11.50081','-85.89014'),(8015,80,'Potosí','potosi','0.00','11.49320','-85.85709'),(8020,80,'Buenos Aires','Buenos-aires','0.00','11.46923','-85.81701'),(8025,80,'Moyogalpa','moyogalpa','0.00','11.53947','-85.69746'),(8030,80,'Altagracia','altagracia','0.00','11.56547','-85.57793'),(8035,80,'San Jorge','San-jorge','0.00','11.45532','-85.80074'),(8040,80,'Rivas','rivas','0.00','11.43975','-85.82880'),(8045,80,'San Juan del Sur','San-juan-del-sur','0.00','11.25384','-85.87177'),(8050,80,'Cárdenas','cardenas','0.00','11.19521','-85.50886'),(8505,85,'Morrito','morrito','0.00','11.62130','-85.08169'),(8510,85,'El Almendro','El-almendro','0.00','11.67684','-84.70362'),(8515,85,'San Miguelito','San-miguelito','0.00','11.40156','-84.90005'),(8520,85,'San Carlos','San-carlos','0.00','11.12088','-84.77837'),(8525,85,'El Castillo','El-castillo','0.00','11.03969','-84.47295'),(8530,85,'San Juan del Norte','San-juan-del-norte','0.00','10.94671','-83.73479'),(9105,91,'Waspán','waspan','0.00','14.74386','-83.96885'),(9110,91,'Puerto Cabezas','Puerto-cabezas','0.00','14.03313','-83.38223'),(9115,91,'Rosita','rosita','0.00','13.91060','-84.39153'),(9120,91,'Bonanza','bonanza','0.00','14.02584','-84.62088'),(9127,91,'Mulukuku','mulukuku','0.00','13.15000','-84.96667'),(9125,91,'Waslala','waslala','0.00','13.33465','-85.37099'),(9130,91,'Siuna','siuna','0.00','13.73857','-84.78491'),(9135,91,'Prinzapolka','prinzapolka','0.00','13.40611','-83.56229'),(9305,93,'Paiwas','paiwas','0.00','12.78548','-85.12402'),(9310,93,'La Cruz de Río Grande','La-cruz-rio-grande','0.00','13.11145','-84.18835'),(9312,93,'Desembocadura de Río Grande','Desembocadura-rio-grande','0.00','12.93208','-83.57697'),(9315,93,'Laguna de Perlas','Laguna-de-perlas','0.00','12.34096','-83.67052'),(9316,93,'El Tortuguero','El-tortuguero','0.00','12.82085','-84.19906'),(9320,93,'Rama','rama','0.00','12.16004','-84.21913'),(9323,93,'El Ayote','El-ayote','0.00','12.49486','-84.81943'),(9325,93,'Muelle de los Bueyes','Muelle-de-los-bueyes','0.00','12.06764','-84.53749'),(9330,93,'Kukra - Hill','Kukra-hill','0.00','12.24163','-83.74532'),(9335,93,'Corn Island','Corn-island','0.00','12.18017','-83.05975'),(9340,93,'Bluefields','bluefields','0.00','12.01144','-83.76388'),(9345,93,'Nueva Guinea','Nueva-guinea','0.00','11.68827','-84.45794'),(1040,10,'Altowangky','altowanky','0.00',NULL,NULL);
/*!40000 ALTER TABLE `lugar_municipio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'lugar','0001_initial','2011-06-09 22:30:50'),(2,'fed','0001_initial','2011-06-09 22:30:52'),(3,'fed','0002_auto__add_tematrabajo','2011-06-09 22:30:56'),(4,'fed','0003_auto__add_poblacionmetaindirecta__add_poblacionmetadirecta','2011-06-09 22:30:57'),(5,'fed','0004_auto__add_resultado','2011-06-09 22:30:58'),(6,'fed','0005_auto__add_field_resultado_codigo','2011-06-09 22:30:59'),(7,'fed','0006_auto__del_field_proyecto_id__chg_field_proyecto_codigo','2011-06-09 22:31:05'),(8,'contraparte','0001_initial','2011-06-09 22:31:06'),(9,'contraparte','0002_auto__add_field_informe_anio_desde__add_field_informe_mes_desde__add_f','2011-06-09 22:31:07'),(10,'contraparte','0003_auto__add_accionimpulsada__add_accionimplementada','2011-06-09 22:31:09'),(11,'contraparte','0004_auto__add_tipoobservatorio__add_observatorio__add_participacioncomisio','2011-06-14 22:28:26'),(12,'fed','0007_auto__del_field_organizacion_telefono__add_field_organizacion_telefono','2011-06-17 15:55:52'),(13,'fed','0008_auto__add_field_proyecto_id__chg_field_proyecto_codigo','2011-06-17 20:42:45'),(14,'fed','0008_auto__chg_field_proyecto_monto_fed__chg_field_proyecto_monto_otros__ch','2011-06-20 20:49:45'),(15,'contraparte','0005_auto__add_demandajusticia__add_acciondemanda__add_denuncia__del_field_','2011-06-21 15:56:31'),(16,'contraparte','0006_auto__add_recibeninfo__add_poseeninfo__add_field_demandajusticia_nombr','2011-06-21 15:56:35'),(17,'contraparte','0007_auto__add_prevencionvbg__add_masculinidadlibre','2011-06-21 15:56:38'),(18,'fed','0009_auto__del_field_organizacion_codigo','2011-06-21 16:08:52'),(19,'contraparte','0008_auto__add_planestrategico__add_denunciainterpuesta__add_referenciacont','2011-06-22 21:25:22');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-06-27  8:46:26
