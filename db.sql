/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - face antispoofing
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`face antispoofing` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `face antispoofing`;

/*Table structure for table `approveduser` */

DROP TABLE IF EXISTS `approveduser`;

CREATE TABLE `approveduser` (
  `auser_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `event_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`auser_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `approveduser` */

/*Table structure for table `event` */

DROP TABLE IF EXISTS `event`;

CREATE TABLE `event` (
  `event_id` int(11) NOT NULL AUTO_INCREMENT,
  `event` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `details` varchar(50) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`event_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `event` */

insert  into `event`(`event_id`,`event`,`place`,`details`,`user_id`) values 
(1,'AssociationCSE','Thodupuzha','UCE College',1);

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `usertype` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'admin@gmail.com','admin','admin'),
(2,'sreethukaruvath@gmail.com','sree4848','user'),
(3,'security1@gmail.com','security','security'),
(4,'security1@gmail.com','security','security'),
(5,'security1@gmail.com','security','security'),
(6,'security1@gmail.com','security','security');

/*Table structure for table `participant` */

DROP TABLE IF EXISTS `participant`;

CREATE TABLE `participant` (
  `participant_id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `image` varchar(1000) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`participant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `participant` */

insert  into `participant`(`participant_id`,`event_id`,`fname`,`lname`,`place`,`gender`,`image`,`status`) values 
(2,1,'dsafs','fdsfds','fsdfds','female','static/trainimages/2/8b38bdbb-936d-4028-8293-bd0edfeed934.jpg','participant'),
(3,1,'Nuthaim','Shukoor','Muvattupuzha','male','static/trainimages/3/7c3c955f-1779-43b0-8ed4-23d9f3469641.jpg','participant'),
(8,1,'anto','varghese','ettumanoor','male','static/trainimages/8/f129dce9-8301-4745-8ce8-94ba1dec6563.jpg','participant');

/*Table structure for table `photo` */

DROP TABLE IF EXISTS `photo`;

CREATE TABLE `photo` (
  `photo_id` int(11) NOT NULL AUTO_INCREMENT,
  `image` varchar(60) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`photo_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `photo` */

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `image` varchar(2000) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`request_id`,`event_id`,`date`,`image`,`status`) values 
(1,1,'2023-04-18','static/notregistered/bab16112-b53b-4791-9f02-5cb48a5ab4b9.png','pending'),
(2,1,'2023-04-18','static/notregistered/14b6dcb2-e254-436f-b817-899db3a70722.png','pending'),
(3,1,'2023-04-18','static/notregistered/09420016-dd67-41b9-a0a5-d3962ab576ae.png','pending'),
(4,1,'2023-04-18','static/notregistered/b5423649-7585-489e-84e3-8534844ef339.png','pending'),
(5,1,'2023-04-18','static/notregistered/185bd2e9-9763-463f-a558-44f51714ae4f.png','pending'),
(6,1,'2023-04-18','static/notregistered/f475226e-84a3-4f67-8631-036dff5059fd.png','pending'),
(7,1,'2023-04-18','static/notregistered/b0b1fb62-badf-4dba-a98c-d3a40dfdc882.png','pending'),
(8,1,'2023-04-18','static/notregistered/3407a127-2e12-42a9-bdd5-4f050c515d50.png','pending'),
(9,1,'2023-04-18','static/notregistered/24457e13-6a3c-49b8-b88a-b61790532f71.png','pending'),
(10,1,'2023-04-18','static/notregistered/b8e57827-4643-4568-abad-81dd76053c45.png','pending');

/*Table structure for table `security` */

DROP TABLE IF EXISTS `security`;

CREATE TABLE `security` (
  `security_id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `fname` varchar(20) DEFAULT NULL,
  `lname` varchar(20) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `login_id` int(20) DEFAULT NULL,
  PRIMARY KEY (`security_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `security` */

insert  into `security`(`security_id`,`event_id`,`fname`,`lname`,`phone`,`email`,`login_id`) values 
(1,0,'Security','1','07306988515','security1@gmail.com',6);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `fname` varchar(100) DEFAULT NULL,
  `lname` varchar(100) DEFAULT NULL,
  `place` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `image` varchar(1500) DEFAULT NULL,
  PRIMARY KEY (`user_id`),
  KEY `foreign` (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user_id`,`login_id`,`fname`,`lname`,`place`,`phone`,`email`,`image`) values 
(1,2,'sreethu','k','malappuram','7306988515','sreethukaruvath@gmail.com','static/trainimages/2/d2737411-3a87-4409-944a-87206a5ea977.jpg');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
