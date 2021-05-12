"""
:author: subofrank
:date: 12/5/2021
:description: for example gin web server get/post
"""
package main

import (
	//"fmt"
	"github.com/gin-gonic/gin"
	"log"
	"net/http"
)

func main() {
	router := gin.Default()
	router.GET("/user/:name", func(c *gin.Context) {
		name := c.Param("name")
		c.String(http.StatusOK, "Hello %s", name)
	})

	router.POST("/user/", func(c *gin.Context) {
		message := c.PostForm("message")
		jack := c.DefaultPostForm("jack", "admin")
		log.Println(message)
		if message == "" {
			c.JSON(200, gin.H{
				"status":  "ok",
				"message": nil,
				"jack":    jack,
			})
		} else {
			c.JSON(200, gin.H{
				"status":  "ok",
				"message": message,
				"jack":    jack,
			})
		}

	})

	router.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}