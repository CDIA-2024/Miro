CREATE DATABASE  IF NOT EXISTS `miru_1.1.1`;
USE `miru_1.1.1`;


--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE `usuario` (
  `id_usuario` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `correo` varchar(45) NOT NULL,
  `contrasena` varchar(45) NOT NULL,
  `año_nacimiento` date NOT NULL,
  `edad` int(11) NOT NULL,
  `genero_de_interes` varchar(45) NOT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Table structure for table `registro`
--

DROP TABLE IF EXISTS `registro`;
CREATE TABLE `registro` (
  `id_registro` int(11) NOT NULL AUTO_INCREMENT,
  `puntuacion` int(11) NOT NULL,
  `estado` varchar(45) NOT NULL,
  `id_usuario` int(11) DEFAULT NULL,
  PRIMARY KEY (`id_registro`),
  KEY `id_usuario` (`id_usuario`),
  CONSTRAINT `id_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Table structure for table 'lista'
--

DROP TABLE IF EXISTS `lista`;
CREATE TABLE `lista` (
  `id_lista` INT(11) NOT NULL AUTO_INCREMENT,
  `fecha_creacion` DATE NOT NULL,
  `id_usuario` INT(11) NOT NULL,
  PRIMARY KEY (`id_lista`),
  FOREIGN KEY (`id_usuario`) REFERENCES `usuario` (`id_usuario`) ON UPDATE CASCADE ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Table structure for table 'contenido'
--

DROP TABLE IF EXISTS `contenido`;
CREATE TABLE `contenido` (
  `id_contenido` INT(11) NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(255) NOT NULL,
  `anio_lanzamiento` YEAR NOT NULL,
  PRIMARY KEY (`id_contenido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Table strucre for table 'anime'
--

DROP TABLE IF EXISTS anime;
CREATE TABLE `anime` (
  `id_anime` INT NOT NULL AUTO_INCREMENT,
  `id_contenido` INT,
  `capitulos` INT,
  `id_estudio` INT,
  PRIMARY KEY (id_anime),
  FOREIGN KEY (id_contenido) REFERENCES contenido(id_contenido),
  FOREIGN KEY (id_estudio) REFERENCES estudioAnimacion(id_estudio)
);

--
-- Table structure for table 'videojuego'
--

DROP TABLE IF EXISTS videojuego;
CREATE TABLE `videojuego`(
  `id_videojuego` INT NOT NULL AUTO_INCREMENT,
  `id_contenido` INT,
  `plataforma` VARCHAR(255),
  `id_desarrollador` INT,
  PRIMARY KEY (id_videojuego),
  FOREIGN KEY (id_contenido) REFERENCES contenido(id_contenido)
);

--
-- Table structure for table 'director'
--

DROP TABLE IF EXISTS director;
CREATE TABLE director (
  id_director INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  PRIMARY KEY (id_director)
);

--
-- Table structure for table 'estudioAnimacion'
--

DROP TABLE IF EXISTS estudioAnimacion;
CREATE TABLE estudioAnimacion (
  id_estudio INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  PRIMARY KEY (id_estudio)
);

--
-- Table structure for table 'productora'
--

DROP TABLE IF EXISTS productora;
CREATE TABLE productora (
  id_productora INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  PRIMARY KEY (id_productora)
);

--
-- Table structure for table 'desarrollador'
--
DROP TABLE IF EXISTS desarrollador;
CREATE TABLE desarrollador (
  `id_desarrollador` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255),
  `id_videojuego` INT,
  PRIMARY KEY(id_desarrollador)
);

--
-- Table strucre for table 'pelicula'
--

DROP TABLE IF EXISTS pelicula;
CREATE TABLE `pelicula` (
  `id_pelicula` INT NOT NULL AUTO_INCREMENT,
  `id_contenido` INT,
  `duracion` INT,
  `id_director` INT,
  PRIMARY KEY (id_pelicula),
  FOREIGN KEY (id_contenido) REFERENCES contenido(id_contenido),
  FOREIGN KEY (id_director) REFERENCES director(id_director)
);

--
-- Table strucre for table 'serie'
--

DROP TABLE IF EXISTS serie;
CREATE TABLE `serie` (
  `id_serie` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(255),
  `id_contenido` INT,
  `temporadas` INT,
  `id_director` INT,
  PRIMARY KEY (id_serie),
  FOREIGN KEY (id_contenido) REFERENCES contenido(id_contenido),
  FOREIGN KEY (id_director) REFERENCES director(id_director)
);

--
-- Modificar la tabla videojuego para añadir la clave foránea id_desarrollador
--
ALTER TABLE `videojuego`
ADD FOREIGN KEY (`id_desarrollador`) REFERENCES `desarrollador`(`id_desarrollador`);
--
-- Modificar la tabla desarrollador para añadir la clave foránea id_videojuego
--
ALTER TABLE `desarrollador`
ADD FOREIGN KEY (`id_videojuego`) REFERENCES `videojuego`(`id_videojuego`);

