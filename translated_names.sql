/*
 Navicat Premium Data Transfer

 Source Server         : names
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 27/03/2023 13:02:23
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for translated_names
-- ----------------------------
DROP TABLE IF EXISTS "translated_names";
CREATE TABLE "translated_names" (
  "english_name" TEXT NOT NULL,
  "arabic_name" TEXT,
  PRIMARY KEY ("english_name")
);

PRAGMA foreign_keys = true;
