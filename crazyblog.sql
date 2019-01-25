# Host: localhost  (Version 5.7.17-log)
# Date: 2018-06-24 19:29:46
# Generator: MySQL-Front 6.0  (Build 2.20)


#
# Structure for table "edit"
#

DROP TABLE IF EXISTS `edit`;
CREATE TABLE `edit` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `description` text,
  `content` longtext,
  `data` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

#
# Data for table "edit"
#


#
# Structure for table "posts"
#

DROP TABLE IF EXISTS `posts`;
CREATE TABLE `posts` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `types` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  `datatime` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

#
# Data for table "posts"
#

INSERT INTO `posts` VALUES (1,'title','type','description','<p>fuck you</p>','June 24, 2018'),(2,'title','type','description','<p>fuck you</p>','June 24, 2018'),(3,'title','fype','description','<p>fuck you</p>','June 24, 2018'),(4,'title','aype','description','<p>fuck you</p>','June 24, 2018'),(5,'title','bbbbbbb','description','<p>fuck you</p>','June 24, 2018'),(6,'title','ta','description','<p>fuck you</p>','June 24, 2018'),(7,'title','type','description','<p>you</p>','June 24, 2018'),(8,'fuck','opq','destude','<p>asdsadsa</p><p>asdasd</p><p>asdasd</p><h3>asdasdsa</h3><p>asdasd</p><p>asdasd</p>','June 24, 2018'),(9,'qweqwe','googd','sadaslkjdlkasj','<p>asdasd</p><p>asdasdasdasdass</p><p>asdasdasdasdasd</p><p>sda</p>','June 24, 2018'),(10,'alskdjsajljl','qweqwioeqwo','dedewqhfkjk','<p>asdas</p><p>asd</p><p>asd</p>','June 24, 2018'),(11,'fuck','alksdjl','asdasda','<p>as</p>','June 24, 2018');
