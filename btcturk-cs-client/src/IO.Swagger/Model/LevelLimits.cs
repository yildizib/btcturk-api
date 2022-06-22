/* 
 * BtcTurk API 3.0
 *
 * White label exchange API documentation.
 *
 * OpenAPI spec version: 3.0
 * Contact: development@btctrader.com
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using SwaggerDateConverter = IO.Swagger.Client.SwaggerDateConverter;

namespace IO.Swagger.Model
{
    /// <summary>
    /// LevelLimits
    /// </summary>
    [DataContract]
        public partial class LevelLimits :  IEquatable<LevelLimits>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="LevelLimits" /> class.
        /// </summary>
        /// <param name="level1Limits">level1Limits.</param>
        /// <param name="level2Limits">level2Limits.</param>
        /// <param name="basicVerifiedLimits">basicVerifiedLimits.</param>
        /// <param name="basicLimits">basicLimits.</param>
        public LevelLimits(LevelLimitValues level1Limits = default(LevelLimitValues), LevelLimitValues level2Limits = default(LevelLimitValues), LevelLimitValues basicVerifiedLimits = default(LevelLimitValues), LevelLimitValues basicLimits = default(LevelLimitValues))
        {
            this.Level1Limits = level1Limits;
            this.Level2Limits = level2Limits;
            this.BasicVerifiedLimits = basicVerifiedLimits;
            this.BasicLimits = basicLimits;
        }
        
        /// <summary>
        /// Gets or Sets Level1Limits
        /// </summary>
        [DataMember(Name="level1Limits", EmitDefaultValue=false)]
        public LevelLimitValues Level1Limits { get; set; }

        /// <summary>
        /// Gets or Sets Level2Limits
        /// </summary>
        [DataMember(Name="level2Limits", EmitDefaultValue=false)]
        public LevelLimitValues Level2Limits { get; set; }

        /// <summary>
        /// Gets or Sets BasicVerifiedLimits
        /// </summary>
        [DataMember(Name="basicVerifiedLimits", EmitDefaultValue=false)]
        public LevelLimitValues BasicVerifiedLimits { get; set; }

        /// <summary>
        /// Gets or Sets BasicLimits
        /// </summary>
        [DataMember(Name="basicLimits", EmitDefaultValue=false)]
        public LevelLimitValues BasicLimits { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class LevelLimits {\n");
            sb.Append("  Level1Limits: ").Append(Level1Limits).Append("\n");
            sb.Append("  Level2Limits: ").Append(Level2Limits).Append("\n");
            sb.Append("  BasicVerifiedLimits: ").Append(BasicVerifiedLimits).Append("\n");
            sb.Append("  BasicLimits: ").Append(BasicLimits).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as LevelLimits);
        }

        /// <summary>
        /// Returns true if LevelLimits instances are equal
        /// </summary>
        /// <param name="input">Instance of LevelLimits to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(LevelLimits input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Level1Limits == input.Level1Limits ||
                    (this.Level1Limits != null &&
                    this.Level1Limits.Equals(input.Level1Limits))
                ) && 
                (
                    this.Level2Limits == input.Level2Limits ||
                    (this.Level2Limits != null &&
                    this.Level2Limits.Equals(input.Level2Limits))
                ) && 
                (
                    this.BasicVerifiedLimits == input.BasicVerifiedLimits ||
                    (this.BasicVerifiedLimits != null &&
                    this.BasicVerifiedLimits.Equals(input.BasicVerifiedLimits))
                ) && 
                (
                    this.BasicLimits == input.BasicLimits ||
                    (this.BasicLimits != null &&
                    this.BasicLimits.Equals(input.BasicLimits))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Level1Limits != null)
                    hashCode = hashCode * 59 + this.Level1Limits.GetHashCode();
                if (this.Level2Limits != null)
                    hashCode = hashCode * 59 + this.Level2Limits.GetHashCode();
                if (this.BasicVerifiedLimits != null)
                    hashCode = hashCode * 59 + this.BasicVerifiedLimits.GetHashCode();
                if (this.BasicLimits != null)
                    hashCode = hashCode * 59 + this.BasicLimits.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }
}